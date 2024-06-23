# # for mail in emails :
# #     if mail[len(mail)-len("@gmail.com"):] == "@gmail.com" :
# #         mail_dung.append(mail)
# # print(mail_dung)
# # mail_dung = []
# # for mail in emails :
# #     if mail[len(mail)-len("@yahoo.com"):] == "@yahoo.com" :
# #         mail_dung.append(mail)
# # print(mail_dung)
#
# # mail = "nguyenminh@yahoo.com" # Đúng
# # print(len(mail))
# # print(len("@yahoo.com"))
# # print(len(mail)-len("@yahoo.com"))
# # print(mail[len(mail)-len("@yahoo.com"):])
# # if mail[len(mail)-len("@yahoo.com"):] == "@yahoo.com" :
# #     print("Mail dung")
# yahoos = [
#     "nguyenminh@yahoo.com",  # Đúng
#     "lethibao@yahoo.com",  # Đúng
#     "tranthanhtu@yahoo.com",  # Đúng
#     "huynhphuong@yahoo.com",  # Đúng
#     "ngoctrai@yahoo.com",  # Đúng
#     "hoangmai@yahoo.com",  # Đúng
#     "thanhson@yahoo.com",  # Đúng
#     "duongkhanh@yahoo.com",  # Đúng
#     "ngocanh@yahoo.com",  # Đúng
#     "haiphuong@yahoo.com",  # Đúng
#     "vietanh@yahoo,com",  # Sai
#     "minhphuong@yahoocom",  # Sai
#     "khanhhoa@yahoo-com",  # Sai
#     "thuha@ yahoo.com",  # Sai
#     "leminh@yahoo. com",  # Sai
#     "phuonglinh@yahoo.com1",  # Sai
#     "hoangnam@yahoo.comabc",  # Sai
#     "anhthu@yahoo,com",  # Sai
#     "minhvu@yahoo,com",  # Sai
#     "baolinh@yhoo.com"  # Sai
# ]
# gmails = [
#     "nguyenanh@gmail.com",  # Đúng
#     "leminhthu@gmail.com",  # Đúng
#     "hoanganh@ymail.com",  # Sai
#     "thanhnam@gmail.com",  # Đúng
#     "bichlien@hotmail.com",  # Sai
#     "giang.nguyen@gmail.com",  # Đúng
#     "kimlien@gmail.com",  # Đúng
#     "minh.tu@gmail",  # Sai
#     "viet.anh.pham@gmail.com",  # Đúng
#     "thuha@gmail.com",  # Đúng
#     "phuonglinh@gmailcom",  # Sai
#     "minhhue@gmail.com",  # Đúng
#     "ducanh.email@gmail.com",  # Đúng
#     "huyen.my@gmail.com",  # Đúng
#     "tranthanh@gmail.com",  # Đúng
#     "huongthao@gmail.com",  # Đúng
#     "ngocthuy@gmail.com",  # Đúng
#     "tuan.kiet@gmail.com",  # Đúng
#     "sonlam@gmail.com",  # Đúng
#     "linhchi@gmail.com",  # Đúng
#     "quang.vu@gmail.com",  # Đúng
#     "tampham@gmail.com",  # Đúng
#     "minh.quan@gmail",  # Sai
#     "thanh.hoa@gmail.com",  # Đúng
#     "linh@gmail.com",  # Đúng
#     "trung@gmail.com",  # Đúng
#     "khanhhoa@gmail.com",  # Đúng
#     "phuongnam@gmail.com",  # Đúng
#     "tuongvy@gmailcom",  # Sai
#     "haiphong@gmail",  # Sai
#     "trungvu@gmail.com",  # Đúng
#     "linhdan@live.com",  # Sai
#     "duy.khoi@outlook.com",  # Sai
#     "thuyhang@gmail.com",  # Đúng
#     "hai.tran@gmail",  # Sai
#     "lananh@yahoo.com",  # Sai
#     "anhthu@gmail.com",  # Đúng
#     "manhtri@gmail.com",  # Đúng
#     "cuongvulive@gmail",  # Sai
#     "lanphuong@icloud.com"  # Sai
# ]
#
# # 1, tao 1 list moi tu 2 list tren
# # 2, lay ra tat cac cac email dung voi duoi la @gmail.com va @yahoo.com
#
# email_tong = gmails + yahoos
# print(email_tong)
#
# email_dung= []
# for email in email_tong:
#     duoi_la_gmail = len(email)-len("@gmail.com")
#     duoi_la_yahoo = len(email)-len("@yahoo.com")
#     if email[duoi_la_gmail:] == "@gmail.com" or email[duoi_la_yahoo:] == "@yahoo.com" :
#         email_dung.append(email)
# print(email_dung)

#Demo cho đăng nhập
# user = ['cuong@gmail.com', '12345678']
#
# user_name = input("Mời nhập UserName:")
# password = input("Mời nhập Password:")
#
# if user_name == user[0] and password == user[1]:
#     print("Đăng nhập thành công")
# else:
#     print("Đăng nhập không thành công")

users = [
    ['cuong@gmail.com', '12345678'],
    ['cuong1@gmail.com', '1234567890'],
    ['nguyenminh@yahoo.com', 'password1'],
    ['lethibao@yahoo.com', 'password2'],
    ['tranthanhtu@gmail.com', 'password3'],
    ['huynhphuong@yahoo.com', 'password4'],
    ['ngoctrai@gmail.com', 'password5'],
    ['hoangmai@yahoo.com', 'password6'],
    ['thanhson@gmail.com', 'password7'],
    ['duongkhanh@yahoo.com', 'password8'],
    ['ngocanh@gmail.com', 'password9'],
    ['haiphuong@yahoo.com', 'password10'],
    ['vietanh@gmail.com', 'password11'],
    ['minhphuong@yahoo.com', 'password12'],
    ['khanhhoa@gmail.com', 'password13'],
    ['thuha@yahoo.com', 'password14'],
    ['leminh@gmail.com', 'password15'],
    ['phuonglinh@yahoo.com', 'password16'],
    ['hoangnam@gmail.com', 'password17'],
    ['anhthu@yahoo.com', 'password18']
]

# Đề bài:  Tương tác người dùng: Nhập user, password.
# Kiểm tra user có đúng format email không? Nếu sai thì trả ra : Sai email
# Kiểm tra mật khẩu > 8 kí tự. Nếu sai thì trả ra : Mật khẩu chưa đủ 8 kí tự
# Đúng cả 2 thì trả ra: Đăng nhập thành công.
# không đúng thì trả ra: Sai password.

user_name = input("Mời nhập UserName:")
password = input("Mời nhập Password:")

ktra_duoi_gmail = len(user_name) - len("@gmail.com")
ktra_duoi_yahoo = len(user_name) - len("@yahoo.com")

if not (user_name[ktra_duoi_gmail:] == "@gmail.com" or user_name[ktra_duoi_yahoo:] == "@yahoo.com"):
    print("sai_email")
else:
    if len(password) < 8 :
        print("Mật khẩu chưa đủ")
    else:
        flag = True
        for user in users :
            if user_name == user[0] and password == user[1]:
                print("Đăng nhập thành công")
                flag = False
            elif user_name == user[0] and password != user[1]:
                print("sai mật khẩu")
                flag = False
        if flag:
            print("Dang nhap khong thanh cong")









