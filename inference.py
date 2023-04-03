import email
import mailparser
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from  nltk.tokenize import word_tokenize
import nltk 
import tldextract
from nltk.stem.snowball import SnowballStemmer
import textdistance
import glob
import datetime


import logging.config

# Define the logging configuration
config = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
}

# Configure logging using the config
logging.config.dictConfig(config)

# Get the logger instance
logger = logging.getLogger('PhishingMailClassifier')

# Log some messages
logger.debug('often makes a very good meal of %s', 'visiting tourists')
logger.info("Project Started\nConstants defined and libraries imported")

URLREGEX = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
URLREGEX_NOT_ALONE = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
GENERAL_SALUTATION = r'\b(dear|hello|Good|Greetings)(?:\W+\w+){0,6}?\W+(user|customer|seller|buyer|account holder)\b'
IPREGEX = r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b"

def getMailBody(mail):
    try:
        parsed_mail = mailparser.parse_from_string(mail)
        mail_body = parsed_mail.body.lower()
        subject = parsed_mail.subject
        headers = parsed_mail.headers
        if parsed_mail.date:
            t = parsed_mail.date.timestamp()
            date_utc = datetime.datetime.utcfromtimestamp(t)
        else:
            date_utc = None
    except (UnicodeDecodeError, OSError) as e:
        parsed_mail = email.message_from_string(mail)
        body = ""
        if parsed_mail.is_multipart():
            for part in parsed_mail.walk():
                # returns a bytes object
                payload = part.get_payload(decode=True)
                if payload is None:
                    continue
                strtext = payload.decode(errors='ignore')
                body += strtext
        else:
            payload = parsed_mail.get_payload(decode=True)
            if payload is None:
                return None, None, None
            strtext = payload.decode(errors='ignore')
            body += strtext
        headers = parsed_mail
        mail_body = body.lower()
        subject = headers['Subject']
        date_utc = None
    return [mail_body, subject, headers, date_utc]


def isURL(link):
    return re.compile(URLREGEX, re.IGNORECASE).search(link) is not None

def getURLs(mail_body):
    result = []
    cleanPayload = re.sub(r'\s+', ' ', mail_body)
    soup = BeautifulSoup(cleanPayload, 'html.parser')
    links = soup.find_all('a')
    i = 0
    for link in links:
        links[i] = link.get('href')
        i += 1

    for link in links:
        if isinstance(link, str) or isinstance(link, bytes):
            if isURL(link):
                result.append(link)
        else:
            continue

    urlregex = re.compile(URLREGEX_NOT_ALONE, re.IGNORECASE)
    links = urlregex.findall(cleanPayload)

    for link in links:
        if link not in result:
            result.append(link)

    res = list(OrderedDict.fromkeys(result))
    result = list(set(result))
    return result

def presenceHTML(mail): #trả về 1 nếu email có chứa mã HTML, ngược lại trả về 0.
    msg = email.message_from_string(mail)
    return int((msg.get_content_type() == 'text/html') == True)

def presenceGeneralSalutation(message):
    return int(re.compile(GENERAL_SALUTATION,re.IGNORECASE).search(message) != None) == True

def mail_to(mail_body):
    return int(re.compile(r'mailto:',
                      re.IGNORECASE).search(mail_body) != None) == True
    
def popups(mail_body): #trả về 1 néu có sự kiện nhấp chuột
    if re.compile(r'window.open|onclick',re.IGNORECASE).search(mail_body):
         return 1
    return 0

stop_words = set(stopwords.words('english')) #set of stopwords
def cleanhtml(sentence): #Hàm này được sử dụng để xóa bỏ các thẻ HTML và trả về một chuỗi đã được làm sạch
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext

def cleanpunc(sentence): # sử dụng để xóa bỏ các ký tự đặc biệt và dấu câu khỏi câu.
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return  cleaned
#sử dụng hai hàm trên để làm sạch văn bản của email, tách các từ ra khỏi văn bản và loại bỏ các từ không cần thiết. Nó trả về một danh sách các từ đã được làm sạch.
def cleanBody(mail_body): 
        filtered = []
        filtered_text = cleanpunc(cleanhtml(mail_body))
        word_tokens = word_tokenize(filtered_text)
        for w in word_tokens:
                if w not in stop_words and w.isalpha():
                    filtered.append(w)
        return filtered
# tính toán sự phong phú của nội dung email bằng cách chia số từ trong email cho số lượng từ duy nhất. Trả về giá trị số thực.
def body_richness(mail_body): 
    mail_body = cleanBody(mail_body)
    if len(set(mail_body))!=0:
        return (len(mail_body)/len(set(mail_body)))
    else:
        return len(mail_body)
    
def isRepliedMail(subject):
    return (subject).startswith('Re:')

def maliciousURL(urls):
    count = 0
    for url in urls:
        if ((re.compile(IPREGEX, re.IGNORECASE).search(url)
             is not None) == True or (len(re.compile(r'(https?://)',re.IGNORECASE).findall(url)) > 1)
                or (len(re.compile(r'(www.)',re.IGNORECASE).findall(url)) > 1)
                or (len(re.compile(r'(\.com|\.org|\.co)',re.IGNORECASE).findall(url)) > 1))== True:
            count += 1
    return count

def textLinkDisparity(mail_body):
    count = 0
    soup = BeautifulSoup(mail_body, 'html.parser')
    lists = soup.find_all('a')
    for item in lists:
        link = item.get('href')
        for string in item.stripped_strings:
            text = str(string)
            text = text.strip().replace('\n', '')
            text = text.strip().replace('\t', ' ')
            if isURL(text) and text != link:
                count += 1
    return count

def numberOfAttachments(raw_mail):
    try:
        mail = mailparser.parse_from_string(raw_mail)
        count = len(mail.attachments)
        return count
    except:
        return 0
    
def IPasURL(urls):
    result = []
    count = 0
    for url in urls:
        if re.compile(IPREGEX, re.IGNORECASE).search(url) and re.compile(IPREGEX, re.IGNORECASE).search(url).group(1) is not None:
            result.append(re.compile(IPREGEX, re.IGNORECASE).search(url).group(1))
            count += 1
    return count

def hexadecimalURL(urls):
    count = 0
    for url in urls:
        if ((re.compile(r'%[0-9a-fA-F]+', re.IGNORECASE).search(url)
             is not None) == True):
            count += 1
    return count

def domainCounts(url):
    domains = tldextract.extract(url)
    count = (len(re.compile(r'\.',re.IGNORECASE).findall( domains.subdomain))) + \
        ((len(re.compile(r'\.',re.IGNORECASE).findall( domains.domain)))+1)
    if re.compile(IPREGEX,re.IGNORECASE).search(domains.domain) is not None:
        count -= 3
    return (count)
def maxDomainsCounts(urls):
    count = 1
    for url in urls:
        count = max(domainCounts(url), count)
    return count

stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()
def purify(subject):
    filtered = ""
    word_tokens = word_tokenize(subject)
    for w in word_tokens:
         if w not in stop_words and w.isalpha():
                   w = stemmer.stem(w)
                   filtered+=(lemmatizer.lemmatize(w))
                   filtered+=" "
    return filtered

def contains_account(subject):
     subject = purify(subject)
     jaro = textdistance.Jaro()
     for w in subject.split():
         
         if (jaro('account',w)) >0.9 or jaro('profile',w) >0.9 or jaro('handle',w) >0.9 :
            return 1
     return 0

def contains_prime_targets(subject):
     subject = purify(subject)
     jaro = textdistance.Jaro()
     for w in subject.split():
         
         if ((jaro('bank',w)) >0.9 or (jaro('Paypal',w)) >0.9 or (jaro('ebay',w)) >0.9 or (jaro('amazon',w)) >0.9):
            return 1
     return 0

def number_of_dots(headers):
    try:
        sender = headers.get("From", "")
        return len(re.compile(r'\.',re.IGNORECASE).findall(sender))
    except KeyError as Argument:
        return 0
def number_of_dash(headers):
    try:
        subject = headers.get("Subject", "")
        return len(re.compile(r'\-',re.IGNORECASE).findall(subject))
    except KeyError as Argument:
        return 0
    
def load_mail(dirpath):
    """load email from the specified path"""
    # Open the file in binary mode and save it to f
    with open(dirpath, 'rb') as f:
        # Read the content of the file as byte and save it to byte_content
        byte_content = f.read()
        # Convert the content of the file from byte to utf-8 string and ignore errors, save it to str_content
        str_content = byte_content.decode('utf-8', errors='ignore')
    # Return str_content as the content of the email
    return str_content


from email import message_from_bytes
from typing import List
import numpy as np
import pandas as pd
import joblib

fields = [
     "Attachments",
          "General_Salutation",
          "HTML",
          "IP_URLs",
          "Malicious_URL",
          "Maximum_Domains_Counts",
          "Number_of_URLs",
          "Re_mail",
          "body_richness",
          "contains_account",
          "contains_prime_targets",
          "hexadecimal_URL",
          "mailto:",
          "number_of_dash",
          "number_of_dots",
          "text_link_disparity"
]

# Load mô hình đã được huấn luyện
model = joblib.load('RandomForestModel.pkl')

def predict_email_label(email_path):
    """
    Dự đoán nhãn cho email dạng eml
    """
    # Đọc file email và chuyển đổi thành object EmailMessage
    mail= load_mail(email_path)

    # Trích xuất các features từ email
    rows = []

    parsed_mail = getMailBody(mail)
    mail_body = parsed_mail[0]
    mail_subject = parsed_mail[1]
    mail_headers = parsed_mail[2]
        
    urls = getURLs(mail_body)
    feature = [0] * (len(fields))
    i = 0
    feature[i] = numberOfAttachments(mail)
    i+=1
    feature[i]= int(presenceGeneralSalutation(mail_body)==True)
    i+=1
    feature[i]= int(presenceHTML(mail)==True)
    i+=1
    feature[i] = (IPasURL(urls))
    i+=1
    feature[i]= (maliciousURL(urls))
    i+=1
    feature[i] = (maxDomainsCounts(urls))
    i+=1
    feature[i]= len(urls)
    i+=1
    feature[i]= int(isRepliedMail(mail_subject)==True)
    i+=1
    feature[i] = body_richness(mail_body)
    i+=1
    feature[i]= int(contains_account(mail_subject)== True)
    i+=1
    feature[i]= int(contains_prime_targets(mail_subject)==True)
    i+=1
    feature[i] = (hexadecimalURL(urls))
    i+=1
    feature[i]= int(mail_to(mail_body)==True)
    i+=1
    feature[i]= number_of_dash(mail_headers)
    i+=1
    feature[i]= number_of_dots(mail_headers)
    #i+=1
    #feature[i]= popups(mail_body)
    i+=1
    feature[i]= textLinkDisparity(mail_body)

             
    rows.append(feature)
    # Dự đoán nhãn của email bằng mô hình đã được huấn luyện
    predicted_label = model.predict(rows)

    # Trả về nhãn dự đoán của email
    return predicted_label[0]
  


    