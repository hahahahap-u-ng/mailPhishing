CHƯƠNG 1: GIỚI THIỆU VẤN ĐỀ NGHIÊN CỨU

	Trong lĩnh vực công nghệ thông tin, sự phát triển luôn đi kèm với rủi ro. Bên cạnh những tiến bộ vượt bậc của công nghệ Điện Toán Đám Mây, Big Data, AI,… là những vụ tấn công mạng xuất hiện thường xuyên hơn, gây hậu quả nặng nề cho người dùng Internet. Chẳng hạn, từ năm 2017 đến năm 2020,
các cuộc tấn công lừa đảo đã tăng từ 72 lên 86% trong số các doanh nghiệp ở Hoa Kỳ mà phần lớn các cuộc tấn công bắt nguồn từ mạng xã hội. Một trong những hình thức tấn công mạng vô cùng phổ biến hiện giờ là tấn công lừa đảo mà tin tặc giả mạo thành một đơn vị uy tín để lừa đảo người dùng cung cấp thông tin cá nhân cho chúng.
	Có nhiều kỹ thuật mà tin tặc sử dụng để thực hiện một vụ tấn công lừa đảo như giả mạo email, giả mạo Website, ... Các email và website giả mạo thường rất giống với chính chủ, chỉ khác một vài chi tiết nhỏ khiên cho người dùng nhầm lẫn và trở thành nạn nhân của cuộc tấn công.  
	Thông thường tin tặc sẽ giả mạo thành các thực thể đáng tin cậy, lừa nạn nhân mở mail, tin nhắn tức thời hoặc tin nhắn văn bản. Người nhận sau đó bị lừa bằng cách nhấp vào liên kết lừa đảo, điều này có thể dẫn đến cài đặt phần mềm độc hại làm đóng băng hệ thống hoặc rò rỉ thông tin nhạy cảm. Một cuộc tấn công có thể gây hậu quả nghiêm trọng đối với cả cá nhân và các tập đoàn lớn
 .
Hình 1: Tổng quan về tấn công lừa đảo

	Tấn công lừa đảo có thể tàn phá nền kinh tế và mất đi tính riêng tư của từng cả nhân và tổ chức. Trong nhiều trường hợp, nếu thành công, tin tặc còn xâm nhập vào quyền riêng tư của nạn nhân và ngăn chặn họ truy cập vào tài khoản của chính mình.
Ngày nay, email được sử dụng rộng rãi như một hình thức giao tiếp cho cá nhân và chuyên gia. Những thông tin trao đổi qua email thường sẽ nhạy cảm và bảo mật như tài khoản ngân hàng, báo cáo tài chinh, chi tiết đăng nhập vv. Điều này khiến chúng có giá trị đối với tin tặc, những người sử dụng thông tin với mục đích xấu. Email lừa đảo được coi là phương pháp tội phạm trực tuyến gia tăng nhanh nhất được sử dụng để đánh cắp dữ liệu tài chính cá nhân và thực hiện hành vi trộm cắp danh tính.  Theo như thống kê của APWG Phishing Activity Trends Report, hình 2 thể hiện được mức độ phát triển của tấn công lừa đảo từ năm 2015 đến 2020 theo quý
  

 
Hình 2: Sự phát triển của tấn công lừa đảo từ năm 2015 đến 2020

	Do đó căn cứ theo mức độ phổ biến và nghiêm trọng của các hình thức lừa đảo, chúng tôi chọn đề tài "Nghiên cứu và xây dựng công vụ phát hiện tấn công lừa đảo" và chuyên sâu đối với chỉ email lừa đảo. Mục tiêu của đề tài là xây dựng một tiện ích mở rộng tự động cảnh báo tới người dùng khi mở email nếu email đó có những dấu hiệu lừa đảo. Băng cách trích xuất những đặc trưng của email và sử dụng các thuật toán học máy phổ biến như như  Naive Bayes, Random Forest, Logistic Regression v v để phân loại, tiện ích này sẽ giảm thiểu tối đa ảnh hưởng tiêu cực như tổn thất tài chính, mất bảo mật thông tin, trộm cắp danh tính v.v.. của các cuộc tấn công lừa đảo.
	Chúng tôi quyết định chọn các thuật toán học máy phổ biến thay vì các thuật toán học sâu vì do : 
•	Do lượng dữ liệu thu thập còn hạn chế
•	Thời gian huấn luyện của học máy ngắn hơn các thuật toán học sâu, và nếu có thể trích xuất được các trường thông tin chính xác thì tỉ lệ chính xác của học máy còn có thể cao hơn kết quả của học sâu. 
•	Số lượng thuật toán học máy lớn nên dễ dàng so sánh tỷ lệ chính xác, đưa ra những thuật toán phù hợp
•	Điều kiện phần cứng hạn chế.




 

CHƯƠNG 2: TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU

I. LÝ THUYẾT BÀI TOÁN:
1. Khái niệm email lừa đảo:
1.1 Email lừa đảo là gì?
Email lừa đảo là một hình thức tấn công Email mà trong đó các hacker thường giả mạo một doanh nghiệp uy tín nào đó để thực hiện các kế hoạch lừa đảo trong Email người dùng. 
Khiến họ tin tưởng và cung cấp các thông tin tài khoản cá nhân, hoặc click vào các liên kết có chứa mã độc, nhằm xâm nhập vào hệ thống mạng doanh nghiệp.
Các hacker này có thể sẽ tạo ra những nội dung email gần giống với giao diện Email của các bên ngân hàng để lừa đảo người dùng khiến họ tin tưởng rằng đó là Email thực sự được gửi từ các ngân hàng mà họ đang có giao dịch. 
Người dùng sẽ dễ dàng chia sẻ các thông tin quan trọng như: mật khẩu đăng nhập hệ thống, mật khẩu giao dịch, thẻ tín dụng và các thông tin tuyệt mật khác.
Email lừa đảo được xem là phương pháp tấn công nguy hiểm và phổ biến nhất hiện nay, nó được phát hiện lần đầu tiên vào năm 1987. Nguồn gốc của từ Phishing là sự kết hợp của 2 từ: fishing for information (câu thông tin) và phreaking (trò lừa đảo). 
Vì có sự tương quan về mặt ý nghĩa giữa việc “câu cá” và “câu thông tin người dùng”, vì thế thuật ngữ Phishing đã ra đời từ đó.
1.2 Các loại Email lừa đảo phổ biến
Có nhiều loại hình thức Email lừa đảo khác nhau được phân loại theo đối tượng và hình thức tấn công. Sau đây là một số hình thức thường gặp:
- Phishing Email giả mạo thông báo Email Doanh Nghiệp overload data
Đây là hình thức email giả mạo thường gặp nhất trong các hệ thống Email doanh nghiệp
Sau khi click vào liên kết Upgrade Email Quota (nâng cấp dung lượng email) là những mã độc được cài đặt sẵn đang chờ đợi xâm nhập vào hệ thống email doanh nghiệp
- Phishing Email giả mạo đặt hàng
Hình thức này thường nhắm vào các doanh nghiệp cung cấp sản phẩm đặt hàng, bởi vì hòm thư email của họ thường xuyên nhận được đơn đặt hàng
Điều này cũng giúp các Phishing Email dễ dàng lọt qua hệ thống bảo mật Email


- Phishing Email giả mạo cơ quan nhà nước
Các Email này được viết sao cho trông nó có vẻ giống nhất với các Email được gửi từ tổ chức chính phủ
Nội dung mang tính chất cảnh báo người dùng như là: “Bạn đã tải xuống các tệp bất hợp pháp, quyền truy cập Internet của bạn sẽ bị thu hồi. Để kháng nghị, bạn hãy điền đầy đủ các thông tin được yêu cầu vào biểu mẫu bên dưới”

 
Hình 3: Ví dụ Email lừa đảo giả mạo cơ quan nhà nước

- Phishing Email giả mạo người quen cũ
Hãy thận trọng với những Email có tên giống với một người bạn, hay đồng nghiệp cũ có nội dung đang trong tình thế cấp bách cần vay một số tiền, hứa sẽ trả lại ngay sau đó.
Để chắc chắn lòng tốt của bạn được đặt đúng chỗ, hãy hỏi người có liên quan trong mối quan hệ này nhé.
- Phishing Email giả mạo thanh toán online
Nếu bạn nhận được một Email thông báo về việc tài khoản thanh toán trực tuyến gặp trở ngại vì thẻ tín dụng đã hết hạn (hoặc địa chỉ thanh toán không đúng,…)
Tiếp theo, nội dung Email còn yêu cầu bạn: “Để khắc phục sự cố này, vui lòng mở đường link và cập nhật thông tin theo yêu cầu”. Bên trong liên kết sẽ là một trang web khá giống với trang đăng nhập thông tin tài khoản mà bạn đã từng thực hiện một vài lần trước đó, điều đó khiến bạn tin tưởng hơn và dễ dàng dính bẫy câu của các hacker

- Phishing Email giả mạo thông báo quá hạn thanh toán
Bạn đang sử dụng Email tên miền doanh nghiệp và một ngày nào đó bạn nhận được những Email thông báo về một dịch vụ đã quá hạn thanh toán
Nội dung Email còn yêu cầu bạn phải đăng nhập vào hệ thống nhanh nhất có thể để lưu trữ lại các dữ liệu quan trọng
Trong Email còn có một liên kết giúp bạn dễ dàng đến trang đăng nhập nhanh nhất có thể. Tuy nhiên, phía sau liên kết đó luôn là một trang web giả mạo nhằm đánh cắp thông tin đăng nhập của bạn

 
Hình 3: Ví dụ Email lừa đảo giả mạo cơ quan nhà nước
- Phishing Email giả mạo thông báo tài khoản bị xâm nhập
Đừng quá hoang mang khi bạn nhận được một Email thông báo rằng tài khoản của bạn đang bị xâm nhập bởi một người lạ
Trong email còn cung cấp đường link để xác minh lại quyền sở hữu. Nếu bạn click vào đó, bạn đã dễ dàng mắc bẫy cửa hacker
- Phishing Email giả mạo thông báo trúng thưởng
Đừng quá phấn khích khi bạn nhận được 1 Email thông báo rằng bạn đã giành được giải thưởng gì đó, vì đây hoàn toàn là một Email giả mạo nhằm kích thích lòng tham của bạn và gây mất cảnh giác
Bạn sẽ dễ dàng nhấp vào liên kết đến website đăng nhập và điền đầy đủ thông tin theo yêu cầu để lãnh giải sớm nhất
- Phishing Email giả mạo thông báo rút tiền
Bạn thường nhận được những thông báo về biến động số dư tài khoản khi bạn thực sự biết trước về giao dịch này
Tuy nhiên, nếu đột nhiên bạn nhận được email thông báo về việc có biến động số dư lớn trong tài khoản của bạn thì đó giống như một thảm họa. Bạn sẽ cố gắng tìm cách ngăn chặn việc rút tiền bất hợp pháp này
Và bên trong Email bạn sẽ thấy có 1 đường link hướng dẫn về việc xác minh hoặc không xác minh đối với hành vi giao dịch này. Biểu mẫu cũng yêu cầu bạn điền đầy đủ các thông tin cần thiết để xác minh quyền sở hữu tài khoản. Và vì thế bạn đã mắc bẫy của các hacker
 
Hình 4: Ví dụ Email lừa đảo thông báo rút tiền

- Phishing Email giả mạo là nạn nhân
Hacker sẽ giả dạng làm một người mua hàng, đặt hàng từ bên bạn nhưng không nhận được bất kì một sản phẩm nào, hoặc bất kỳ phản hồi nào từ phía bạn. Email còn cảnh báo rằng họ sẽ báo cáo lên chính quyền địa phương nếu bạn không có một lời giải thích nào với họ
Trong Email còn có một liên kết cho bạn dễ dàng thực hiện việc phản hồi cho "người mua hàng" đó, bạn đăng nhập tài khoản và sau đó tài khoản của bạn đã bị đánh cắp
- Phishing Email giả mạo chi cục Thuế
Thường gặp ở các bộ phận kế toán tài chính doanh nghiệp. Khi mà họ thường ngày vẫn phải đối mặt với những vấn đề về Thuế, thông báo từ chi cục Thuế. Họ dễ dàng bị mắc bẫy và cung cấp thông tin quan trọng cho hacker
- Phishing Email giả mạo checkup
Một ngày bạn nhận được một email báo rằng hệ thống email doanh nghiệp đang tiến hành checkup (kiểm tra) hệ thống và để xác mình quyền sở hữu với email mà bạn đang được cấp phát sử dụng
Hãy điền vào biểu mẫu theo yêu cầu để xác minh. Nếu bạn làm theo những yêu cầu trong Email này, bạn đã vừa để mất toàn bộ thông tin đăng nhập tài khoản Email của mình
1.3. Cách xác định, nhận biết một Email lừa đảo
Việc đính kèm các đường link, file chứa virus hay các phần mềm độc hại là một chiêu trò lừa đảo rất phổ biến từ các hacker. Những phần mềm này sẽ gây hại, làm hỏng những file trong máy của bạn
Hoặc nhờ chúng mà các tội phạm lấy được mật khẩu, các thông tin cá nhân. Một điều nguy hiểm hơn là may bạn có thể bị cài những phần mềm gián điệp
Vì vậy không được mở những file lạ được đính kèm trong các Email. Nếu bạn muốn kiểm tra những liên kết này, hãy mở một cửa sổ khác. Sau đó nhập trực tiếp địa chỉ lên đây thay vì bấm vào liên kết từ Email
- Khai báo những thông tin cá nhân
Một ngân hàng hợp pháp hay một doanh nghiệp uy tín sẽ không bao giờ yêu cầu bạn phải đưa thông tin cá nhân qua Email
Vì vậy bạn cũng tuyệt đối không được cung cấp bất kỳ thông tin cá nhân khi có những yêu cầu khai báo thông tin
- Cẩn thận với những lời lẽ thể hiện sự khẩn cấp
Những Email lừa đảo thường sẽ có những câu nói tạo ra cảm giác cấp bách, sợ hãi cho người nhận. Đây là một chiến thuật lừa đỏa vô cùng tinh vi
Bạn cần cảnh giác trước những câu nói như “tài khoản của bạn đang tạm thời bị ngừng truy cập”. Hoặc có trường hợp là “ nỗ lực đăng nhập trái phép”…
 
Hình 5: Ví dụ Email lừa đảo 



- Để ý thông tin chi tiết
Email không có những thông tin liên hệ cụ thể hoặc chữ ký không rõ ràng. Đây chính là biểu hiện của một hình thức Phishing Email. Bởi nếu là một doanh nghiệp hợp pháp chắc chắn sẽ cung cấp thông tin liên hệ chi tiết
1.4. Cách phòng chống Phishing Email
- Đối với cá nhân
•	Không click vào bất kỳ đường link nào được gửi qua Email nếu bạn không chắc chắn 100% an toàn
•	Không bao giờ gửi thông tin bí mật qua Email
•	Không trả lời những thư lừa đảo. Những kẻ gian lận thường gửi cho bạn số điện thoại để bạn gọi cho họ vì mục đích kinh doanh. Họ sử dụng công nghệ Voice over Internet Protocol. Với công nghệ này, các cuộc gọi của họ không bao giờ có thể được truy tìm
•	Sử dụng Tường lửa và phần mềm diệt virus. Hãy nhớ luôn cập nhật phiên bản mới nhất của các phần mềm này
- Đối với các tổ chức, doanh nghiệp
•	Training cho nhân viên để tăng kiến thức sử dụng Internet an toàn. Thường xuyên tổ chức các buổi tập huấn, diễn tập các tình huống giả mạo
•	Sử dụng dịch vụ G-suite dành cho doanh nghiệp, không nên sử dụng dịch vụ Gmail miễn phí vì dễ bị giả mạo
•	Triển khai bộ lọc SPAM để phòng tránh thư rác, lừa đảo
•	Luôn cập nhật các phần mềm, ứng dụng để tránh các lỗ hổng bảo mật có thể bị kẻ tấn công lợi dụng
•	Chủ động bảo mật các thông tin nhạy cảm, quan trọng. Xem thêm Giải pháp bảo mật thông tin cho doanh nghiệp
•	
2. Lý thuyết các thuật toán
2.1 Logistic Regression
a.	Lý thuyết Hồi quy tuyến tính: 
Hai mô hình tuyến tính (linear models) Linear Regression và Perceptron Learning Algorithm (PLA) chúng ta đã biết đều có chung một dạng:
 
trong đó f() được gọi là activation function, và x được hiểu là dữ liệu mở rộng với x0=1 được thêm vào để thuận tiện cho việc tính toán. Với linear regression thì f(s)=s, với PLA thì f(s)=sgn(s). Trong linear regression, tích vô hướng wTx được trực tiếp sử dụng để dự đoán output y, loại này phù hợp nếu chúng ta cần dự đoán một giá trị thực của đầu ra không bị chặn trên và dưới. Trong PLA, đầu ra chỉ nhận một trong hai giá trị 1 hoặc −1, phù hợp với các bài toán binary classification.

Trong bài này, tôi sẽ giới thiệu mô hình thứ ba với một activation khác, được sử dụng cho các bài toán flexible hơn. Trong dạng này, đầu ra có thể được thể hiện dưới dạng xác suất (probability). Ví dụ: xác suất thi đỗ nếu biết thời gian ôn thi, xác suất ngày mai có mưa dựa trên những thông tin đo được trong ngày hôm nay,… Mô hình mới này của chúng ta có tên là logistic regression. Mô hình này giống với linear regression ở khía cạnh đầu ra là số thực, và giống với PLA ở việc đầu ra bị chặn (trong đoạn [0,1]. Mặc dù trong tên có chứa từ regression, logistic regression thường được sử dụng nhiều hơn cho các bài toán classification.
  b. Sigmoid function
Trong số các hàm số có 3 tính chất nói trên thì hàm sigmoid:
 
được sử dụng nhiều nhất, vì nó bị chặn trong khoảng (0,1)(0,1). Thêm nữa:
 


Đặc biệt hơn nữa: 
 

Công thức đạo hàm đơn giản thế này giúp hàm số này được sử dụng rộng rãi. Ở phần sau, tôi sẽ lý giải việc người ta đã tìm ra hàm số đặc biệt này như thế nào.

Ngoài ra, hàm tanh cũng hay được sử dụng:
 

Hàm số này nhận giá trị trong khoảng (−1,1) nhưng có thể dễ dàng đưa nó về khoảng (0,1). Bạn đọc có thể chứng minh được:
 


2.2 SVC
    	   a. Lý thuyết SVM: 
SVM là một thuật toán giám sát, nó có thể sử dụng cho cả việc phân loại hoặc đệ quy. Tuy nhiên nó được sử dụng chủ yếu cho việc phân loại. Trong thuật toán này, chúng ta vẽ đồi thị dữ liệu là các điểm trong n chiều ( ở đây n là số lượng các tính năng bạn có) với giá trị của mỗi tính năng sẽ là một phần liên kết. Sau đó chúng ta thực hiện tìm "đường bay" (hyper-plane) phân chia các lớp. Hyper-plane nó chỉ hiểu đơn giản là 1 đường thẳng có thể phân chia các lớp ra thành hai phần riêng biệt.
 
Hình 6: Ví dụ đường Huper- plane
Support Vectors hiểu một cách đơn giản là các đối tượng trên đồ thị tọa độ quan sát, Support Vector Machine là một biên giới để chia hai lớp tốt nhất.
b. SVM làm việc như thế nào
Ở trên, chúng ta đã thấy được việc chia hyper-plane. Bấy giờ làm thế nào chúng ta có thể xác định "Làm sao để vẽ-xác định đúng hyper-plane". Chúng ta sẽ theo các tiêu chí sau:
•	Identify the right hyper-plane (Scenario-1):
Ở đây, có 3 đường hyper-lane (A,B and C). Bây giờ đường nào là hyper-lane đúng cho nhóm ngôi sao và hình tròn.
 
Hình 7: Xác định đường hyper-plane đúng (Trường hợp 1) 
Quy tắc số một để chọn 1 hyper-lane, chọn một hyper-plane để phân chia hai lớp tốt nhất. Trong ví dụ này chính là đường B.
•	Identify the right hyper-plane (Scenario-2):
Ở đây chúng ta cũng có 3 đường hyper-plane (A,B và C), theo quy tắc số 1, chúng đều thỏa mãn.

 
Hình 8: Xác định đường huper-plane đúng (Trường hơp 2)
Quy tắc thứ hai chính là xác định khoảng cách lớn nhất từ điểu gần nhất của một lớp nào đó đến đường hyper-plane. Khoảng cách này được gọi là "Margin", Hãy nhìn hình bên dưới, trong đấy có thể nhìn thấy khoảng cách margin lớn nhất đấy là đường C. Cần nhớ nếu chọn lầm hyper-lane có margin thấp hơn thì sau này khi dữ liệu tăng lên thì sẽ sinh ra nguy cơ cao về việc xác định nhầm lớp cho dữ liệu.
•	Identify the right hyper-plane (Scenario-3):
Sử dụng các nguyên tắc đã nêu trên để chọn ra hyper-plane cho trường hợp sau:
 
Hình 9: Xác định đường hyper-plane đúng (Trường hợp 3)
Có thể có một vài người sẽ chọn đường B bởi vì nó có margin cao hơn đường A, nhưng đấy sẽ không đúng bởi vì nguyên tắc đầu tiên sẽ là nguyên tắc số 1, chúng ta cần chọn hyper-plane để phân chia các lớp thành riêng biệt. Vì vậy đường A mới là lựa chọn chính xác.
•	Can we classify two classes (Scenario-4)?
Tiếp the hãy xem hình bên dưới, không thể chia thành hai lớp riêng biệt với 1 đường thẳng, để tạo 1 phần chỉ có các ngôi sao và một vùng chỉ chứa các điểm tròn.
 
Hình 10: Phân biệt hai nhóm đối tượng
Ở đây sẽ chấp nhận, một ngôi sao ở bên ngoài cuối được xem như một ngôi sao phía ngoài hơn, SVM có tính năng cho phép bỏ qua các ngoại lệ và tìm ra hyper-plane có biên giới tối đa . Do đó có thể nói, SVM có khả năng mạnh trong việc chấp nhận ngoại lệ.
 
Hình 11: Phân biết hai nhóm đối tượng có ngoại lệ
•	Find the hyper-plane to segregate to classes (Scenario-5)
Trong trường hợp dưới đây, không thể tìm ra 1 đường hyper-plane tương đối để chia các lớp, vậy làm thế nào để SVM phân tách dữ liệu thành hai lớp riêng biệt? Cho đến bây giờ chúng ta chỉ nhìn vào các đường tuyến tính hyper-plane.
 
Hình 12: Tách dữ liệu thành 2 lớp bằng đường hyper-plane
SVM có thể giải quyết vấn đề này, Khá đơn giản, nó sẽ được giải quyết bằng việc thêm một tính năng, Ở đây chúng ta sẽ thêm tính năng z = x^2+ y^2. Bây giờ dữ liệu sẽ được biến đổi theo trục x và z như sau
 
Hình 13: Tách dữ liệu thành 2 lớp bằng đường hyper-plane 2
Trong sơ đồ trên, các điểm cần xem xét là: • Tất cả dữ liệu trên trục z sẽ là số dương vì nó là tổng bình phương x và y • Trên biểu đồ các điểm tròn đỏ xuất hiện gần trục x và y hơn vì thế z sẽ nhỏ hơn => nằm gần trục x hơn trong đồ thị (z,x) Trong SVM, rất dễ dàng để có một siêu phẳng tuyến tính (linear hyper-plane) để chia thành hai lớp, Nhưng một câu hỏi sẽ nảy sinh đấy là, chúng ta có cần phải thêm một tính năng phân chia này bằng tay hay không. Không, bởi vì SVM có một kỹ thuật được gọi là kernel trick ( kỹ thuật hạt nhân), đây là tính năng có không gian đầu vào có chiều sâu thấm và biến đổi nó thành không gian có chiều cao hơn, tức là nó không phân chia các vấn đề thành các vấn đề riêng biệt, các tính năng này được gọi là kernel. Nói một cách đơn giản nó thực hiện một số biết đổi dữ liệu phức tạp, sau đó tìm ra quá trình tách dữ liệu dựa trên các nhãn hoặc đầu ra mà chúng ra đã xác định trước.
c. Margin trong SVM
 
Hình 14: Margin trong SVM
Margin là khoảng cách giữa siêu phẳng đến 2 điểm dữ liệu gần nhất tương ứng với các phân lớp. Trong ví dụ quả táo quả lê đặt trên mặt bán, margin chính là khoảng cách giữa cây que và hai quả táo và lê gần nó nhất. Điều quan trọng ở đây đó là phương pháp SVM luôn cố gắng cực đại hóa margin này, từ đó thu được một siêu phẳng tạo khoảng cách xa nhất so với 2 quả táo và lê. Nhờ vậy, SVM có thể giảm thiểu việc phân lớp sai (misclassification) đối với điểm dữ liệu mới đưa vào
d. Lập trình tìm nghiệm cho bài toán SVM
Tìm nghiệm cho SVM ta sử dụng trực tiếp thư viện sklearn.
Chúng ta sẽ sử dụng hàm*** sklearn.svm.SVC*** ở đây. Các bài toán thực tế thường sử dụng thư viện libsvm được viết trên ngôn ngữ C, có API cho Python và Matlab.
from sklearn.svm import SVC

model = SVC(kernel='linear', probability=True)
model.fit(emb_array, labels)
#Do somethings....
w = model.coef_
b = model.intercept
print('w = ', w)
print('b = ', b)
2.3 Gradient Boosting
a. AdaBoost - Gradient Boosting
Cả AdaBoost và Gradient Boosting đều xây dựng thuật toán nhằm giải quyết bài toán tối ưu sau :
 
Trong đó :
•	L : giá trị loss function
•	y : label
•	cn : confidence score của weak learner thứ n (hay còn gọi là trọng số)
•	wn : weak learner thứ n
Thoạt nhìn, công thức trên có vẻ khá giống với Bagging, thế nhưng cách tính ra các giá trị confidence score kia lại làm nên sự khác biệt về hướng giải quyết của Boosting. Thay vì cố gằng quét tìm tất cả các giá trị cn,wn để tìm nghiệm tối ưu toàn cục - một công việc tốn nhiều thời gian và tài nguyên, chúng ta sẽ cố gắng tìm các giá trị nghiệm cục bộ sau khi thêm mỗi một mô hình mới vào chuỗi mô hình với mong muốn dần đi đến nghiệm toàn cục.
 
b.Adaptive Boosting
AdaBoost tiến hành train các mô hình mới dựa trên việc đánh lại trọng số cho các điểm dữ liệu hiện tại, nhằm giúp các mô hình mới có thể tập trung hơn vào các mẫu dữ liệu đang bị học sai, từ đó làm giảm giá trị loss của mô hình. Cụ thể, các bước triển khai thuật toán như sau :
•	Khởi tạo weight ban đầu là bằng nhau (bằng 1/N) cho mỗi điểm dữ liệu
•	Tại vòng lặp thứ i
o	train model wi (weak learner) mới được thêm vào
o	tính toán giá trị loss (error), từ đó tính toán ra giá trị confidence score ci của model vừa train
o	Cập nhật model chính W=W+ci∗wi
o	Cuối cùng, đánh lại trọng số cho các điểm dữ liệu (Các điểm dữ liệu bị đoán sai --> tăng trọng số, các điểm dữ liệu đoán đúng --> giảm trọng số).
•	Sau đó lặp lại với vòng lặp thêm model tiếp theo i + 1.
 
Hình 15: Vòng lặp model  trong Adaptive Boosting
FYI: AdaBoost có thể được áp dụng mà không cần dựa vào việc đánh trọng số lại các điểm dữ liệu, thay vào đó, chúng ta có thể re-sample để lấy dữ liệu train cho các model tiếp theo dựa vào xác suất được xác định bới các trọng số.
c. Gradient Boosting
Gradient Boosting là một dạng tổng quát hóa của AdaBoost. Cụ thể như sau, vẫn vấn đề tối ưu ban đầu
 
Trước tiên mình xin nhắc lại một chút lí thuyết mà các bạn đã khá quen trong neural network: Gradient Descent
 
Phía trên là công thức cập nhật tham số mô hình theo hướng giảm của đạo hàm (Gradient Descent). Công thức này được sử dụng không gian tham số, tuy nhiên, để liên hệ với bài toán chúng ta đang xét, mình chuyển công thức sang góc nhìn của không gian hàm số.
Khá đơn giản thôi, nếu chúng ta coi chuỗi các model boosting là một hàm số W, thì mỗi hàm learner có thể coi là một tham số w. Đến đây, để cực tiểu hóa hàm loss L(y,W), chúng ta áp dụng Gradient Descent
 
Đến đây, ta có thể thấy mối quan hệ liên quan sau
 
với wn là model được thêm vào tiếp theo. Khi đó, model mới cần học để fit để vào giá trị -η∂w∂L(Wn−1). (Giá trị -η∂w∂L(Wn−1) còn có 1 tên gọi khác là pseudo-residuals)
Tóm lại, chúng ta có thể tóm tắt quá trình triển khai thuật toán như sau:
•	Khởi tạo giá trị pseudo-residuals là bằng nhau cho từng điểm dữ liệu
•	Tại vòng lặp thứ i
•	Train model mới được thêm vào để fit vào giá trị của pseudo-residuals đã có
•	Tính toán giá trị confidence score ci của model vừa train
•	Cập nhật model chính W=W+ci∗wi
•	Cuối cùng, tính toán giá trị pseudo-residuals −η∂w∂L(Wn−1) để làm label cho model tiếp theo
•	Sau đó lặp lại với vòng lặp i + 1.
Nếu bạn để ý thì phương pháp cập nhật lại trọng số của điểm dữ liệu của AdaBoost cũng là 1 trong các case của Gradient Boosting. Do đó, Gradient Boosting bao quát được nhiều trường hợp hơn.
2.4  ExtraTrees Classifier
ExtraTrees Classifier là một thuật toán phân loại được sử dụng trong Machine Learning. Đây là một biến thể của thuật toán Random Forest Classifier, mà nó tạo ra một lượng lớn các cây quyết định (decision trees) và chọn các tập con ngẫu nhiên của đặc trưng (features) tại mỗi nút để chia dữ liệu.

Các cây quyết định được xây dựng bằng cách chọn ngẫu nhiên các đặc trưng và các mẫu (samples) trong dữ liệu huấn luyện. Sau đó, cây được sử dụng để dự đoán nhãn cho các mẫu mới dựa trên các đặc trưng của chúng. Kết quả cuối cùng là sự trung bình hoặc phiếu đa số của các cây quyết định.

ExtraTrees Classifier thường cho kết quả tốt khi sử dụng trên các tập dữ liệu lớn và có nhiều đặc trưng. Thuật toán này cũng không dễ dẫn đến overfitting như các thuật toán khác. Tuy nhiên, vì nó phụ thuộc vào sự chọn lựa ngẫu nhiên của đặc trưng, kết quả có thể không ổn định trong một số trường hợp.
2.5	 Random Forest Classifier
Random Forest Classifier là một thuật toán học máy phân loại dữ liệu. Nó được xây dựng dựa trên việc kết hợp nhiều cây quyết định (decision tree) để tạo ra một mô hình dự đoán chính xác.

Trong quá trình huấn luyện, Random Forest sẽ tạo ra nhiều cây quyết định, mỗi cây sẽ được xây dựng trên một tập dữ liệu con được lấy ngẫu nhiên từ tập dữ liệu huấn luyện ban đầu. Mỗi cây sẽ được xây dựng bằng cách chọn các đặc trưng (features) và giá trị ngưỡng (thresholds) để phân tách tập dữ liệu.

Sau khi tạo ra các cây quyết định, Random Forest sử dụng phương pháp "voting" để quyết định nhãn của một điểm dữ liệu mới. Điểm dữ liệu sẽ được phân loại vào lớp được ủng hộ nhiều nhất bởi các cây quyết định.

Với sự kết hợp của nhiều cây quyết định, Random Forest Classifier có thể tránh được overfitting (quá khớp) và có khả năng dự đoán chính xác cao. Nó được sử dụng phổ biến trong các bài toán phân loại, ví dụ như phân loại ảnh, dữ liệu y tế, tài chính, và marketing.
2.6  Ensemble Model (Voting Classifier) (hard voting và soft voting)
Ensemble Model là một kỹ thuật trong học máy, trong đó nhiều mô hình dự đoán được kết hợp lại để tạo ra một dự đoán cuối cùng.

Voting Classifier là một loại Ensemble Model, nơi các mô hình được kết hợp bằng phương pháp bỏ phiếu (voting) để tạo ra một dự đoán cuối cùng. Voting Classifier có thể được chia thành hai loại: hard voting và soft voting.

•	Hard voting: Ở đây, dự đoán cuối cùng được đưa ra bằng cách bỏ phiếu đơn giản trên các mô hình thành viên. Ví dụ, nếu trong tập các mô hình thành viên có 3 mô hình cho kết quả là A và 2 mô hình cho kết quả là B, thì dự đoán cuối cùng sẽ là A.
 
Hình 16: Hard voting

•	Soft voting: Ở đây, các dự đoán của các mô hình thành viên được trọng số khác nhau để tính toán dự đoán cuối cùng. Trong trường hợp này, các mô hình đưa ra các dự đoán xác suất cho mỗi lớp, và kết quả cuối cùng được tính toán bằng cách tính trung bình trọng số các dự đoán xác suất. Trong trường hợp này, mô hình có độ chính xác cao hơn sẽ được trọng số nhiều hơn.
 
Hình 17: Soft Voting
Voting Classifier là một cách tốt để kết hợp các mô hình khác nhau để tạo ra một dự đoán cuối cùng. Nó được sử dụng phổ biến trong các bài toán phân loại, và có thể cải thiện độ chính xác và độ ổn định của dự đoán.
II. Thực trạng vấn đề nghiên cứu
Phát hiện email lừa đảo gần đây nhận được nhiều sự chú ý bởi sự ảnh hưởng của nó đối với bảo mật an toàn người dùng. Vì thế có rất nhà khoa học và nhiều kỹ thuật được phát triển để phát hiện email lừa đảo 
Azad đã tập trung vào việc thử nghiệm các thuật toán có độ chính xác khác nhau như Naive Bayes, logistic regression và support vector machine (SVM) với một lượng lớn dữ liệu. Nhìn chung, các thuật toán phân loại đạt được kết quả cao với tỷ lệ chính xác là 95% với SVM với kernel và Bayes. Đây là hai thuật toán đưa ra tỷ lệ cao nhất. Khi so sánh với Naive Bayes và Logistic Regression, SVM cho thấy kết quả bằng nhau khi được thử nghiệm trên tập dữ liệu ít thuộc tính hơn. Tóm lại, nghiên cứu cho thấy SVM có ưu thế cho việc phát hiện email lừa đảo trước khi được gửi vào hộp thư đến của người dùng.
Giáo sư Wu tập trung vào việc giả mạo email và dịch vụ Microsoft OutlookTM bằng cách phát triển một giao thức xác thực người gửi (SAP). Giao thức xác thực này xác minh người gửi bằng cách kiểm tra sự xác nhận với các email được lưu trữ. Các OutlookTM nâng cao có một phần bổ trợ kiểm tra tính khả thi trong khi nó vẫn giữ nguyên giao diện thân thiện với người dùng của phiên bản gốc và phần bổ trợ SAP này sẽ được bắt đầu tự động khi OutlookTM hoạt động
Vào năm 2015, Kathirvalavakumar và những người khác đã đề xuất một mạng lưới thần kinh đa lớp để phát hiện email lừa đảo. Mạng lưới được đề xuất dựa trên thuật toán cắt xén feedforward trích xuất dữ liệu và đặc trưng của email và áp dụng weight trimming giúp giảm số lượng các đặc trưng thông qua thuật toán và tính toán tối thiểu cần thiết để phân loại email có lừa đảo hay không. Vì mạng này đã được thử nghiệm trên dữ liệu từ năm 2007, sử dụng mạng này cho dữ liệu hiện tại yêu cầu xác định các tính năng mới cho thuật toán kết hợp chúng vào miền đầu vào để đào tạo để trở nên hữu ích.
Một mô hình phát hiện lừa đảo đã được đề xuất bởi Nizamani (2014) bằng cách lựa chọn các tính năng trong đó và các đặc trưng khác nhau được so sánh về mặt tỷ lệ nhằm phát hiện email lừa đảo. Nghiên cứu được tiến hành áp dụng một số thuật toán phân loại chẳng hạn như SVM, NB, J48 và CCM, ngoài các đặc trưng khác nhau. Tỷ lệ phần trăm chính xác là 96% đã đạt được và kết quả chỉ ra rằng mức độ chính xác bị ảnh hưởng bởi các đặc trưng  hơn là các thuật toán phân loại

III. Phát triển giả thuyết nghiên cứu
Công việc của đề tài bắt đầu bằng cách xem qua các tài liệu nghiên cứu khác nhau và điều tra email lừa đảo. Sau đó, xác định tập hợp các đặc trưng trong email lừa đảo.
Thư được tải xuống từ nhiều nguồn khác nhau và bộ dữ liệu CSV được xây dựng bởi các đặc trưng trích xuất . Bộ dữ liệu được trực quan hóa và sử dụng kỹ thuật giảm kích thước. Tầm quan trọng của thuộc tính hiển thị trường hợp các tính năng quan trọng trong quá trình phân loại. Nhiều thuật toán phân loại sau đó được triển khai trên tập dữ liệu. Top 4 phân loại các thuật toán được chọn trên cơ sở lỗi xác thực chéo. Tích hợp các mô hình được chọn để tạo thành một mô hình tập hợp để có hiệu suất tốt hơn.

 
CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU

I.  XÂY DỰNG MÔ HÌNH HỌC MÁY: 
1. Thu thập dữ liệu:
Bộ dữ liệu được sử dụng trong kho chứa tổng cộng 3.000 email, một nửa trong số đó là email lừa đảo và nửa còn lại là email hợp pháp. Tập dữ liệu được lưu trữ trong tệp CSV có tên "mail_dataset.csv".
Các email lừa đảo được thu thập từ các cơ sở dữ liệu và kho lưu trữ lừa đảo khác nhau, chẳng hạn như PhishTank và OpenPhish. Các email hợp pháp được thu thập từ bộ dữ liệu email có sẵn công khai, chẳng hạn như bộ dữ liệu email Enron. Các email trong bộ dữ liệu được gắn nhãn là lừa đảo hoặc hợp pháp dựa trên nội dung và các đặc điểm khác của chúng. 

2. Tiền xử lý dữ liệu:
Trong bước tiền xử lý, bộ dữ liệu email lừa đảo được thu thập. Word Cloud Analysis giúp ta hiểu rõ hơn về cả hai loại thư ham và phishing để xác định được các thuộc tính quan trọng. Word Cloud Analysis từ là một kỹ thuật được sử dụng để trực quan hóa và phân tích dữ liệu văn bản bằng cách tạo ra một biểu diễn đồ họa của các từ xuất hiện phổ biến nhất trong một kho văn bản. Trong Word Cloud Analysis, kích thước của mỗi từ trong Word Cloud tỷ lệ thuận với tần suất xuất hiện của nó trong văn bản. Điều này cho phép người dùng nhanh chóng xác định các chủ đề hoặc chủ đề phổ biến nhất trong văn bản, cũng như các ngoại lệ hoặc các mẫu bất thường.
 	


Hình 18: Word Cloud ucra Ham Mails và Phishing Mails

Bước đầu tiên trong quá trình tiền xử lý dữ liệu là trích xuất đặc trưng. Chúng tôi đã trích xuất các tính năng khác nhau từ tiêu đề và nội dung email, chẳng hạn như địa chỉ email của người gửi, dòng chủ đề và nội dung email. Các tính năng đã được chọn dựa trên mức độ phù hợp của chúng với khả năng phát hiện lừa đảo và tính khả dụng của chúng trong bộ dữ liệu. Đặc trưng sau đó được trích xuất từ mỗi email và được trình bày trong một danh sách của mảng, mỗi hàng đại diện cho một email cùng với các cột tương ứng là các thuộc tính được chọn, thêm một cột thể hiện loại email (liệu email lừa đảo hoặc email hợp pháp) như thể hiện trong Bảng sau





Tính năng	Miêu tả
HTML	kiểm tra xem email có chứa mã HTML không
HTMLForm	kiểm tra xem email có chứa biểu mẫu HTML không
Iframe	kiểm tra xem email có chứa IFrame không
Javascript	kiểm tra xem email có chứa mã JavaScript không
Flash Content	kiểm tra xem email có chứa nội dung Flash không
General Salutation	kiểm tra xem email có chứa lời chào thông thường không
Attachments	số lượng có chứa đính kèm không
Popups	kiểm tra xem email có chứa của sổ bật lên không
Body Richness	kiểm tra xem email có chứa định dạng văn bản phong phú (HTML) hay không
Bảng 1: Đặc trưng thân email

Tính năng	Miêu tả
Number of URLs	số lượng URL có trong email
Malicious URL	kiểm tra xem email có chứa URL độc hại không
Text link disparity	kiểm tra sự khác biệt giữa văn bản liên kết và liên kết thực tế
IP URLs	kiểm tra xem email có chứa địa chỉ IP trong URL không
Hexadecimal in URLs	kiểm tra xem email có chứa URL ở dạng hex không
Bad Rank Domain	kiểm tra tên miền có được xếp hạng không tốt không
Max Domains Counts	số lượng tên miền tối đa có trong email
@'_in_url	kiểm tra xem email có chứa ký tự "@" trong URL không
Mail to	kiểm tra xem email có chứa đường dẫn thư đến không
Bảng 2: Đặc trưng URL

Tính năng	Miêu tả
Re mail	kiểm tra xem email có phải là email trả lời không
Fwd mail	kiểm tra xem email có phải là email chuyển tiếp không
Contains account	kiểm tra xem dòng chủ đề có tài khoản trong đó
Contains verify	kiểm tra xem dòng chủ đề có xác minh trong đó không
Contains Update	kiểm tra xem  dòng chủ đề có cập nhật trong đó không
Contains prime targets	kiểm tra xem email dòng chủ đề có mục tiêu chính (amazon, bank, paypal, ...)
Contains suspended	kiểm tra dòng chủ đề đã bị đình chỉ
Contains password	kiểm tra xem dòng chủ đề có mật khẩu trong đó không
Contains urgent	kiểm tra xem dòng chủ đề có chứa từ "urgent" không
Contains access	kiểm tra xem dòng chủ đề  có chứa từ "access" không
Subject richness	Thể hiện sự phong phú của dòng chủ đề
Bảng 3: Đặc trung của chủ đề

Tính năng	Miêu tả
Number of dash	Hiển thị số lượng dấu gạch ngang trong địa chỉ
Number of dots	Hiển thị số lượng dấu chấm trong địa chỉ

Bảng 4: Đặc trưng địa chỉ người gửi

Chúng tôi đã trích xuất tổng cộng 18 đặc trưng bao gồm: số ký tự trong tiêu đề, số ký tự trong nội dung, số liên kết trong nội dung, số liên kết ngoài trong nội dung, số liên kết ảnh trong nội dung, số liên kết ảnh ngoài trong nội dung, số liên kết video trong nội dung, số liên kết video ngoài trong nội dung, số liên kết âm thanh trong nội dung, số liên kết âm thanh ngoài trong nội dung, có chứa IP hay không, có chứa @ hay không, có chứa // hay không, có chứa - hay không, có chứa  hay không, có chứa ? hay không, có chứa = hay không và có chứa & hay không.

Chúng tôi đã thực hiện một số thao tác làm sạch cơ bản trên tập dữ liệu, chẳng hạn như xóa các email trùng lặp và kiểm tra các giá trị bị thiếu. Chúng tôi cũng đã xóa một số tính năng không liên quan khỏi tập dữ liệu, chẳng hạn như ID email và ngày tháng.

Dữ liệu được đọc từ một tệp csv có tên là emails.csv, chứa hai cột: text và label. Cột text là nội dung của thư điện tử, còn cột label là nhãn có thể bị lừa đảo hay không (0 hoặc 1), au đó được chia thành hai tập: tập huấn luyện (80% dữ liệu) và tập kiểm tra (20% dữ liệu). Tập huấn luyện được sử dụng để huấn luyện các mô hình học máy, còn tập kiểm tra được sử dụng để đánh giá hiệu quả của các mô hình. Sau đó, dữ liệu được tiền xử lý bằng cách loại bỏ các ký tự không phải chữ cái, chuyển đổi sang chữ thường, loại bỏ các từ dừng (stopwords) và áp dụng kỹ thuật lemmatization để biến đổi các từ về dạng gốc của chúng. Dữ liệu được trích xuất đặc trưng bằng cách sử dụng hai phương pháp: CountVectorizer và TfidfVectorizer. Hai phương pháp này đều biến đổi các văn bản thành các vector số, nhưng có cách tính khác nhau. CountVectorizer chỉ đếm số lần xuất hiện của mỗi từ trong văn bản, còn TfidfVectorizer còn tính trọng số của mỗi từ dựa trên tần suất xuất hiện trong toàn bộ tập dữ liệu.
Dữ liệu được thêm một số đặc trưng khác như số lượng chữ cái viết hoa, số lượng chữ cái viết thường, số lượng ký tự đặc biệt, số lượng số, số lượng từ và tần suất xuất hiện của các từ khóa có thể liên quan đến thư điện tử lừa đảo. Các đặc trưng này được kết hợp với các vector số đã được biến đổi để tạo thành một ma trận đặc trưng cho mỗi văn bản.
 	Đặc trưng sau đó được trích xuất từ mỗi email và được trình bày trong một danh sách của mảng, mỗi hàng đại diện cho một email cùng với các cột tương ứng là các thuộc tính được chọn, thêm một cột thể hiện loại email (liệu email lừa đảo hoặc email hợp pháp) như thể hiện trong Bảng 21
 
Hình 19: Các đặc trưng được trích xuất từ email

Chúng tôi sử dụng heatmap để xác định các tính năng có mối tương quan cao trong tập dữ liệu, có thể ảnh hưởng đến tính ổn định và khả năng diễn giải của các mô hình học máy. Bằng cách loại bỏ một trong các tính năng khỏi mỗi cặp tương quan cao, chúng tôi có thể giảm đặc trưng và cải thiện hiệu suất của các mô hình.

Heatmap cũng cung cấp thông tin chi tiết về mối quan hệ giữa các tính năng khác nhau trong bộ dữ liệu. Ví dụ:  các tính năng 'IP_Address' và 'URL' có mối tương quan cao, điều này không có gì đáng ngạc nhiên vì nhiều cuộc tấn công lừa đảo sử dụng các URL giả chuyển hướng đến các địa chỉ IP độc hại. Hay 'Từ sai chính tả' và 'Miền sai' có mối tương quan tích cực, điều này cho thấy các tính năng này nắm bắt thông tin tương tự về sự hiện diện của lỗi chính tả hoặc tên miền không chính xác trong email.
Sau quá trình xử lý dữ liệu, chúng tôi chọn những thuộc tính sau:
'Attachments',
 'General Salutation',
 'HTML',
 'IP URLs',
 'Malicious URL',
 'Maximum Domains Counts',
 'Number of URLs',
 'Re: mail',
 'body richness',
 'contains account',
 'contains prime targets',
 'hexadecimal URL',
 'mailto:',
 'number of dash',
 'number of dots',
 'text link disparity' 
Bằng cách chọn các tính năng có nhiều thông tin nhất, chúng tôi đã có thể cải thiện độ chính xác và hiệu suất của các mô hình máy học của họ trong việc xác định email lừa đảo.
	3. Đưa vào mô hình và đánh giá hiệu suất
Quyết định chọn 5 mô hình phân loại điều chỉnh siêu tham số:
Logistic Regression
SVC
Gradient Boosting
ExtraTrees Classifier
Random Forest Classifier
Sau đây là hiệu suất các mô hình trước khi hiệu chỉnh siêu tham số:
3.1. Logistic Regression
Logistic Regression là một kỹ thuật khác được máy học mượn từ lĩnh vực thống kê. Đây là phương pháp đi đầu cho các bài toán phân loại nhị phân (các bài toán có hai giá trị lớp).
. 
Hình 20: Hiệu suất của mô hình Logistic Regressiontruwowsc khi đièu chỉnh tham số và sau 10 lần  CV

3.2. SVC
	Mô hình SVC là viết tắt của Support Vector Classifier, một loại máy vector hỗ trợ (SVM) dùng để phân loại dữ liệu. Mô hình này tìm một siêu phẳng (hyperplane) để phân chia hai lớp trong không gian nhiều chiều sao cho khoảng cách giữa siêu phẳng và các điểm gần nhất của hai lớp là lớn nhất1. Mô hình này có thể sử dụng các hàm nhân (kernel) khác nhau để biến đổi không gian dữ liệu và tìm các siêu phẳng phi tuyến tính
 
Hình : Hiệu suất của mô hình SVC trước khi đièu chỉnh tham số và sau 10 lần  CV
3.3. Gradient Boosting
Gradient Boosting là một kỹ thuật học máy dùng để cải thiện độ chính xác của các mô hình dự đoán, thường là các cây quyết định. Mô hình này xây dựng một tập hợp của nhiều cây quyết định yếu (weak learners) theo cách tuần tự, sao cho mỗi cây tiếp theo cố gắng khắc phục sai số của cây trước đó. Mô hình này cho phép tối ưu hóa một hàm mất mát bất kỳ có thể vi phân được.
 
Hình : Hiệu suất của mô hình Gradient Boosting trước khi đièu chỉnh tham số và sau 10 lần CV
3.4. ExtraTrees Classifier
	ExtraTrees Classifier là một loại bộ phân loại dựa trên nhiều cây quyết định ngẫu nhiên (extra-trees) được kết hợp lại trong một rừng (forest). Mô hình này tương tự như Random Forest Classifier nhưng khác ở chỗ cách xây dựng các cây quyết định trong rừng. ExtraTrees Classifier chọn ngẫu nhiên các thuộc tính và các điểm phân chia tại mỗi nút của cây, trong khi Random Forest Classifier chọn các thuộc tính và các điểm phân chia tốt nhất tại mỗi nút của cây.
 
	Hình : Hiệu suất của mô hình ExtraTrees Classifier trước khi điều chỉnh tham số và sau 10 lần CV

3.5 Random Forest Classifier
Random Forest Classifier là một loại bộ phân loại dựa trên nhiều cây quyết định được kết hợp lại trong một rừng (forest). Mô hình này sử dụng kỹ thuật bagging để tạo ra các tập con ngẫu nhiên của dữ liệu huấn luyện và xây dựng một cây quyết định cho mỗi tập con. Sau đó, mô hình tổng hợp các dự đoán của các cây quyết định bằng cách lấy số đa số (majority vote) cho bài toán phân loại hoặc lấy trung bình (average) cho bài toán hồi quy.
 
Hình : Hiệu suất của mô hình Random Forest Classifier trước khi điều chỉnh tham số và sau 10 lần CV

* So sánh các chỉ số đánh giá mô hình phân loại
 	Logistic Regression	SVC	Gradient Boosting	ExtraTrees Classifier	Random Forest Classifier
MCC	0.922	0.943	0.941	0.96	0.958
Log loss	0.124	0.106	0.077	0.144	0.175
f1	96.372	97.436	97.291	98.226	98.117
balance Accuracy	96.207	97.137	97.194	97.943	97.807
Accuracy	96.074	97.178	97.055	98.037	97.914
ROC_AUC	96.207	97.137	97.149	97.943	97.807


Hình : So sánh các chỉ số đánh giá mô hình tham số mặc định
4. Hiệu chỉnh tham số và đánh giá hiệu suất
Việc điều chỉnh tham số quan trọng là rất quan trọng vì chúng kiểm soát hành vi tổng thể của các mô hình học máy. Một tham số quan trọng là một tham số có giá trị được đặt trước khi quá trình học bắt đầu. Mục tiêu cuối cùng là tìm ra sự kết hợp tối ưu của các tham số quan trọng để giảm thiểu một hàm mất mát được xác định trước để cho kết quả tốt hơn
Chúng tôi đã sử GridSearchCV, một công cụ tìm kiếm lưới tham số để tìm các tham số tối ưu cho mô hình. Công cụ này thử mọi kết hợp có thể của mỗi tập tham số quan trọng. Bằng cách sử dụng phương pháp này, chúng ta có thể tìm ra bộ giá trị tốt nhất trong không gian tìm kiếm tham số. Phương pháp này thường sử dụng nhiều tài nguyên tính toán và mất nhiều thời gian để chạy vì phương pháp này cần thử mọi kết hợp trong kích thước lưới.
Các tham số quan trọng rất quan trọng vì chúng kiểm soát hành vi tổng thể của một mô hình học máy. Mục tiêu cuối cùng là tìm ra sự kết hợp tối ưu của các tham số quan trọng để giảm thiểu một hàm mất mát được xác định trước để cho kết quả tốt hơn.
Điều chỉnh hiệu suât các mô hình cùng với tham số tốt nhất như sau
4.1. Logistic Regression
Các giá trị tối ưu cho các tham số của mô hình Logistic Regression như sau:
•	Penalty: l2 regularization
•	C: 0.1
•	solver: lbfgs
 
Hình 26: Hiệu suất của Logistic Regression sau khi điều chỉnh siêu tham số
4.2. SVC
Các giá trị tối ưu cho các tham số của mô hình SVC như sau:
•	Kernel: 'rbf'
•	C: 1.0
•	Gamma: 'scale'

 
Hình 26: Hiệu suất của SVC sau khi điều chỉnh siêu tham số

4.3. Gradient Boosting
Các giá trị tối ưu cho các tham số của mô hình Gradient Boosting như sau:
•	Learning Rate: 0.1
•	Maximum Depth: 5
•	Maximum Features: None
•	Minimum Samples Leaf: 1
•	N Estimators: 200

 
Hình 26: Hiệu suất của Gradient Boosting sau khi điều chỉnh siêu tham số

4.4. ExtraTrees Classifier
	Các giá trị tối ưu cho các tham số của mô hình ExtraTrees Classifier  như sau:
•	n_estimators: 100
•	max_depth: 20
•	min_samples_split: 2
•	min_samples_leaf: 1
•	max_features: 'auto'

 
Hình 26: Hiệu suất của ExtraTrees Classifier sau khi điều chỉnh siêu tham số

4.5 Random Forest Classifier
Các giá trị tối ưu cho các tham số của mô hình ExtraTrees Classifier như sau:
•	n_estimators: 100
•	max_depth: 20
•	min_samples_split: 2
•	min_samples_leaf: 1
•	max_features: 'auto'

 
Hình 26: Hiệu suất của Random Forest Classifier sau khi điều chỉnh siêu tham số

* So sánh các chỉ số đánh giá mô hình phân loại


 
Hình 31: Đường cong học tập của các mô hình đã điều chỉnh
Nếu chúng ta tập trung một chút vào đường cong học tập, chúng ta sẽ thấy rằng:
•	Sau một kích thước huấn luyện cụ thể, SVC cân bằng giữa việc đánh đổi giữa sai số và phương sai và các đường cong gần như có khoảng cách giống nhau cho đến kích thước huấn luyện phù hợp.
•	ExtraTrees cũng hoạt động tốt nhưng sau một điểm, việc huấn luyện quá nhiều dẫn đến tăng sai số một chút và sau đó dẫn đến hiện tượng underfitting.
•	Random Forest cũng tuân theo xu hướng gần như giống như SVC, đạt được sự cân bằng hợp lý giữa sai số và phương sai.
•	Cuối cùng, Logistic Regression và GradientBoosting có xu hướng overfitting.
Vì vậy, cho bộ phân loại bỏ phiếu (voting classifier), chúng ta sẽ đi với ba mô hình:
•	SVC (C=3, gamma=0.1, probability=True)
•	ExtraTrees Classifier (max_features=1, min_samples_split=10, n_estimators=300)
•	Random Forest Classifier (bootstrap=False, max_features=3, min_samples_leaf=3,min_samples_split=3)
Ba mô hình trên đều có độ chính xác cân bằng tốt và cũng làm tốt trong việc cân bằng giữa sai số và phương sai.

Thay vì tạo các mô hình riêng biệt và tìm độ chính xác cho từng cái, chúng tôi sử dụng tập hợp biểu quyết (ếnmble) của các mô hình phân loại được chọ để tăng cường hiệu suất. Cụ thể, chúng tôi sử dụng 3 mô hình là Gradient Boosting, ExtraTrees Classifier và Random Forest Classifier để xây dựng tập hợp biểu quyết.
	Các dự đoán từ ba mô hình này được kết hợp bằng phương pháp "soft voting" để tạo ra dự đoán cuối cùng. Trong phương pháp này, mỗi mô hình đóng góp vào dự đoán bằng cách tính toán xác suất cho mỗi lớp, sau đó tổng hợp các xác suất này để đưa ra dự đoán cuối cùng.
Sau đó, sử dụng các thước đo hiệu suất như accuracy, precision, recall, F1-score, balanced accuracy, ROC AUC và MCC để đánh giá hiệu suất của tập hợp biểu quyết và so sánh với các mô hình đơn lẻ. Kết quả cho thấy rằng tập hợp biểu quyết có hiệu suất tốt hơn so với các mô hình đơn lẻ và là mô hình tốt nhất trong dự án

  
Hình 32: Hiệu suất của mô hình Voting Classifier trên dữ liệu thử nghiệm
Trực quan hóa hiệu suất bằng biểu đồ học tập
 
Hình : Đường cong học tập các mô hình Voting Classifier
Cả hai mô hình trên đều cho kết quả gần như giống nhau. Mặc dù chúng có độ chính xác thấp hơn một chút, nhưng chúng có sự cân bằng tốt giữa bias và variance trade off. Chúng có thể rất hữu ích trong các ứng dụng thực tế vì chúng không có xu hướng overfitting dữ liệu huấn luyện trong khi giảm thiểu khoảng cách giữa lỗi huấn luyện và lỗi cross validation. Do đó, có thể suy ra rằng chúng sẽ hoạt động tốt hơn trong các ứng dụng thực tế.

	5. Kết luận với các thuật toán
	Khi các mô hình được đào tạo, xác thực chéo và thử nghiệm, bây giờ chúng ta sẽ so sánh nó. Do bộ dữ liệu khá mất cân bằng, cho nên chúng ta tránh tập trung vào độ chính xác thay vì tập trung vào các thông số khác như Acurracy, log los, f1, .... Chúng sẽ thể hiện tốt hơn hiệu suất mô hình
 
Hình : Bảng so sánh hiệu suất của các mô hình khác nhau
Mặc dù tất cả các mô hình đều hoạt động tốt sau khi điều chỉnh tham số quan trọng, chúng tôi nhận thấy rằng Voting Classifier không vượt trội hơn các ước lượng mà nó thu thập phiếu bầu.  Voting Classifier thực hiện khá tương đồng trong cả hard voting và soft voting và cân bằng tốt giữa độ lệch và phương sai.
 
Hình  : Biểu đồ nhiệt hiệu suât các mô hình khác nhau

Trong quá trình nghiên cứu, cả ExtraTrees Classifier và Random Forest đều rất gần nhau về hiệu suất. Mặc dù độ chính xác cân bằng của cả ExtraTrees Classifier và Random Forest là như nhau nhưng Random Forest có điểm log loss tốt hơn so với ExtraTrees.
Random Forest được chọn là mô hình tốt hơn để xác định email giả mạo khi xét đến các đặc trưng được chọn hơn ExtraTrees vì nó có sự cân bằng tốt của sai số và phương sai. SVC cũng sẽ là một lựa chọn rất tốt trong thực tế như đã được nghiên cứu, nó cân bằng một cách trơn tru sự đánh đổi giữa sai số và phương sai do đó nó học được trong quá trình huấn luyện mà không bị quá khớp và có thể hoạt động rất tốt với dữ liệu mới.
Biểu đồ thanh ở trên cho thấy hiệu suất của các mô hình dựa trên điểm số độ chính xác cân bằng. Chúng ta có thể thấy mỗi mô hình đều cải thiện hiệu suất sau khi điều chỉnh.
Những suy luận sau được rút ra từ nghiên cứu:
1.	Mô hình có hiệu suất tốt nhất là Random Forest Classifier được điều chỉnh tham số với độ chính xác là 98.469% và log loss là 0.066. và các tham số là (bootstrap= False, max_features= 3, min_leaf_sample= 3, min_sample_split= 3)
2.	Mặc dù Random Forest có hiệu suất tốt nhất trong thí nghiệm nghiên cứu của chúng tôi, nhưng SVM và Voting Classifier lại có hiệu quả hơn trong việc cân bằng sự đánh đổi giữa sai số và phương sai.
3.	Logistic Regression và Gradient Boosting có xu hướng quá khớp nên tốt hơn là tránh hoặc sử dụng một cách có thể chống lại sự quá khớp. Ví dụ, chúng ta có thể bao gồm chúng trong model stacking hoặc voting classifier và chống lại sự quá khớp bằng cách điều chỉnh trọng số.
4.	Cuối cùng, rõ ràng là để có mô hình hoạt động tốt hơn trong thực tế, chúng ta có thể chọn Voting Classifier. Chúng ta có thể có hiệu suất tốt hơn với dữ liệu kiểm tra mới trong khi hy sinh độ chính xác tối thiểu.
II. QUÁ TRÌNH XÂY DỰNG HỆ THỐNG VÀ THỬ NGHIỆM:
1 .Tổng quan về hệ thống
Mục đích của hệ thống là để cảnh báo người sử dụng email tránh truy cập vào các email có nội dung lừa đảo nhằm hạn chế thiệt hại về tài sản và tránh lộ thông tin của cá nhân của bản thân. Hệ thống được triển khai xây dựng trên chrome extensions khi được triển khai người dùng có thể lựa chọn mô hình để kiểm tra email mà mình nhận được có phải là email lừa đảo hay không khi được phát hiện là lừa đảo sẽ đưa ra cảnh báo cho người dùng tránh truy cập vào email đó làm hạn chế tối đa mức thiệt hại mà người sử dụng có thể gặp phải

2. Nền tảng công nghệ
•	Giao diện Client:
o	HTML (Hyper Text Markup Language)
o	CSS (Cascading Style Sheets)
o	JS (JavaScript)
o	Chrome extensions
•	Server:
o	Python
o	Flask
o	NodeJs
•	Database:
o	MongoDB
•	Khác:
o	Docker
3. Giao diện hệ thống
•	Phần giao diện lựa chọn extensions chọn model để thực thi


 
                        Hình: Lựa chọn model kiểm tra email

•	Thông báo khi cảnh báo email lừa đảo

 

                   Hình: Thông báo khi phát hiện ra email là lừa đảo

4.Xây dựng hệ thống và thử nghiệm
Xây dựng chrome extensions khi người dùng truy cập vào gmail của mình để xem các email về công việc hay trao đổi thông tin với ai đó khi họ click vào 1 email bất kì thì sẽ có một module lấy nội dung thành phần email gửi về phía server
 
                                              Hình: Email muốn kiểm tra

khi sever tiếp nhận thông tin thì nó sẽ tạo 1 file .eml chứa những thông tin dữ liệu của email đó.
 
                     Hình: file .eml được tạo ra để chứa nội dung của email cần kiểm tra
 Sau đó file .eml sẽ được sử dụng để kiểm tra xem nội dung của email có chứa nội dung nào là lừa đảo hay không bằng một hàm inference được train để phát hiện các email lừa đảo. Khi phát hiện lừa đảo thì phía sever sẽ gọi 1 API trả về thông báo cho clients.
 
                  Hình: thông báo được trả về ngay khi phát hiện email lừa đảo




CHƯƠNG 4: KẾT QUẢ VÀ ĐÁNH GIÁ
1. Kết quả:
Đề tài xây dựng và phát tiển thành công một tiện ích mở rộng phát hiện email lừa đảo. Sau khi phân tích và xử lý tập dữ liệu, chúng đã huấn luyện và đánh giá năm mô hình học máy khác nhau, bao gồm Logistic Regression, SVC, Random Forest, Gradient Boosting và ExtraTrees Classifier.
Kết quả đánh giá cho thấy các mô hình đều đạt được độ chính xác và độ tin cậy tương đối cao trong việc phát hiện email lừa đảo. Tuy nhiên, mô hình Random Forest đã cho kết quả tốt nhất với độ chính xác 98,3% và AUC-ROC là 99,9%. Các giá trị này cho thấy rằng mô hình Random Forest có khả năng phát hiện email lừa đảo rất tốt. Từ đó áp dụng các nền tảng công nghệ, thiết kế giao diệ hệ thống thân thiệ với ngươi dùng để xây dựng extensions kiểm tra email và đưa ra cảnh báo
2. Đánh giá: 
Tuy nhiên, dự án cũng có một số hạn chế và điểm yếu. Đầu tiên, tập dữ liệu được sử dụng không quá lớn, do đó mô hình có thể không phản ánh đầy đủ thực tế. 
Thứ hai, cần phải đánh giá và kiểm tra mô hình trên các tập dữ liệu khác để đảm bảo rằng nó hoạt động tốt và có khả năng tổng quát hóa. Cuối cùng, cần xem xét các phương pháp khác để xử lý dữ liệu đầu vào để cải thiện độ chính xác của mô hình. 
Thứ ba, hiện nay, mô hình học máy sử dụng trong đề tài đều hoạt động dựa trên việc kiểm tra văn bản (text) trong email để phát hiện xem email đó có phải phishing hay không. Nhưng trong thực tế các tin tặc thường sử dụng ảnh hoặc video để truyền tải thông điệp lừa đảo thay vì dùng text như trước đây. Do đó sản phẩm mà đề tài đưa ra không đảm bảo được độ chính xác cao.


















CHƯƠNG 5: KẾT LUẬN VÀ KHUYẾN NGHỊ

1. Kết luận:
Đề tài nhằm mục đích tiến hành một đánh giá so sánh giữa các kỹ thuật thuật toán phân loại và các đặc trưng khác nhau để phát hiện email phishing bằng cách sử dụng các đặc trưng của email và URL. Chúng tôi cũng đề xuất một mô hình tích hợp nhiều phân loại bằng cách kết hợp nhiều kỹ thuật phân loại để tăng cường khả năng phát hiện và bảo vệ chống lại email phishing
Đề tài được thực hiện bằng cách sử dụng Python và Jupyter Notebook. CHúng tôi đã trích xuất các đặc trưng từ tiêu đề, nội dung và URL của các email, và đã sử dụng các phương pháp tiền xử lý dữ liệu, như loại bỏ ký tự đặc biệt, chuyển đổi sang chữ thường, loại bỏ stop words, áp dụng stemming và lemmatization. Sử dụng các phương pháp phân tích dữ liệu, như tạo biểu đồ tần suất, ma trận tương quan, kiểm tra giả thuyết và kiểm tra độ tin cậy. Đề tài sử dụng các phương pháp đánh giá mô hình, như MCC, Log loss, f1, balance Accuracy, Accuracy, ROC_AUC.
Kết quả nghiên cứu cho thấy rằng các đặc trưng URL có ảnh hưởng lớn hơn đến khả năng phát hiện email phishing so với các đặc trưng email .Đề tài cũng so sánh hiệu suất của các thuật toán phân loại khác nhau, như Logistic Regression, SVC, Gradient Boosting, ExtraTrees Classifier, Random Forest Classifier và chỉ ra rằng Random Forest có hiệu suất cao nhất với độ chính xác là 97,6%.Đề tài cũng xây dựng một mô hình tích hợp bằng cách kết hợp Random Forest, SVC và Logistic Regression, và cho thấy rằng mô hình này có hiệu suất tốt hơn so với các mô hình đơn lẻ..
Từ mô hình có hiệu suất lớn nhất đã được huấn luyện và lưu lại, triển khai và xây dựng tiện ích mở rộng (extensions). Tiện ích này giúp người dùng có thể lựa chọn mô hình để kiểm tra email mà mình nhận được có phải là email phishing hay không bằng cách đưa ra thông báo trên cửa sổ màn hình, hạn chế tối đa thiệt hại cho người dùng.

2. Khuyến nghị:
Đề tài đã thực hiện một nghiên cứu tốt về việc phân loại email là bình thường hoặc giả mạo bằng các mô hình học máy. Tuy nhiên, vẫn còn một số khuyến nghị mà người lập trình có thể thực hiện để cải thiện dự án này:
Nghiên cứu thêm các kỹ thuật tiền xử lý dữ liệu: Tiền xử lý dữ liệu là một bước quan trọng trong việc chuẩn bị dữ liệu cho mô hình học máy,  có thể nghiên cứu thêm các kỹ thuật tiền xử lý dữ liệu khác nhau như chuẩn hóa dữ liệu, xử lý dữ liệu bị thiếu, loại bỏ nhiễu, chuyển đổi đặc trưng, v.v.
Sử dụng các mô hình học sâu: Mô hình học sâu như mạng nơ-ron sâu có thể giúp tăng độ chính xác của mô hình và phân loại email đích danh và không phải đích danh tốt hơn, có thể thực hiện nghiên cứu thêm về mô hình học sâu để nâng cao hiệu suất của dự án.
Mở rộng tập dữ liệu: Tập dữ liệu trên có số lượng dữ liệu không lớn và có thể không đại diện cho các trường hợp khác nhau,  có thể mở rộng tập dữ liệu bằng cách thu thập dữ liệu từ các nguồn khác hoặc tạo dữ liệu mới để đảm bảo mô hình có khả năng tổng quát hóa tốt hơn.
Đánh giá sự ổn định của mô hình: Một số mô hình học máy có thể bị ảnh hưởng bởi sự thay đổi trong dữ liệu huấn luyện, có thể đánh giá sự ổn định của mô hình bằng cách áp dụng các phương pháp khác nhau để đánh giá hiệu suất của mô hình trên các tập dữ liệu khác nhau.
	Mở rộng tính chính xác của hệ thống bằng cách sử dụng các mô hình học máy nhằm phát hiện lừa đảo thông qua ảnh và video.
