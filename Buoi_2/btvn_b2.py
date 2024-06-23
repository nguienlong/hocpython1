# users = [
#     ['cuong@gmail.com', '12345678', 0],
#     ['cuong1@gmail.com', '1234567890', 0],
#     ['nguyenminh@yahoo.com', 'password1', 0],
#     ['lethibao@yahoo.com', 'password2', 0],
#     ['tranthanhtu@gmail.com', 'password3', 0],
#     ['huynhphuong@yahoo.com', 'password4', 0],
#     ['ngoctrai@gmail.com', 'password5', 0],
#     ['hoangmai@yahoo.com', 'password6', 0],
#     ['thanhson@gmail.com', 'password7', 0],
#     ['duongkhanh@yahoo.com', 'password8', 0],
#     ['ngocanh@gmail.com', 'password9', 1],
#     ['haiphuong@yahoo.com', 'password10', 1],
#     ['vietanh@gmail.com', 'password11', 1],
#     ['minhphuong@yahoo.com', 'password12', 1],
#     ['khanhhoa@gmail.com', 'password13', 1],
#     ['thuha@yahoo.com', 'password14', 1],
#     ['leminh@gmail.com', 'password15', 1],
#     ['phuonglinh@yahoo.com', 'password16', 1],
#     ['hoangnam@gmail.com', 'password17', 1],
#     ['password18', 'password18', 1]
# ]
#
# # Lam tuong tu, bai tren. Neu tai khoan la 0 : print(Đăng nhập thành công User thuong)
# # Lam tuong tu, bai tren. Neu tai khoan la 1 : print(Đăng nhập thành công User Admin)
#
#
#
# user_name = input("Mời nhập UserName:")
# password = input("Mời nhập Password:")
#
# # user_name[len(user_name) - len("@gmail.com")]:)
# # ktra_duoi_yahoo = len(user_name) - len("@yahoo.com")
#
# if not (user_name[len(user_name) - len("@gmail.com"):] == "@gmail.com" or user_name[len(user_name) - len("@yahoo.com"):] == "@yahoo.com") :
#     print("sai_email")
# else:
#     if len(password) < 8 :
#         print("Mật Khẩu chưa đủ 8 kí tự")
#     flag = True
#     for user in users :
#         if user_name == user [0] and password == user [1]:
#             if user [-1] == 0:
#                 print("Đăng nhập thành công tài khoan User thường")
#                 flag = False
#             else:
#                 print("Đăng nhập thành công User Admin")
#                 flag = False
#         elif user_name == user [0] and password != user [1]:
#             print("Sai Mật khẩu")
#             flag = False
#     if flag:
#         print("Đăng nhập không thành công")



x = {'Person_1': [8, 4, 8, 2, 10], 'Person_2': [7, 8, 2, 10, 3], 'Person_3': [0, 7, 5, 4, 6],
     'Person_4': [4, 4, 4, 10, 6], 'Person_5': [9, 8, 5, 3, 4], 'Person_6': [7, 4, 2, 6, 9],
     'Person_7': [1, 3, 0, 5, 3], 'Person_8': [3, 3, 2, 1, 8], 'Person_9': [3, 4, 3, 8, 5],
     'Person_10': [10, 7, 8, 3, 10], 'Person_11': [0, 1, 9, 3, 8], 'Person_12': [4, 10, 3, 4, 10],
     'Person_13': [7, 0, 6, 5, 6], 'Person_14': [7, 9, 9, 2, 6], 'Person_15': [9, 1, 0, 7, 8],
     'Person_16': [7, 8, 9, 7, 6], 'Person_17': [1, 4, 1, 10, 6], 'Person_18': [8, 9, 7, 0, 2],
     'Person_19': [1, 2, 5, 4, 6], 'Person_20': [9, 1, 6, 2, 10], 'Person_21': [4, 9, 0, 3, 10],
     'Person_22': [3, 3, 9, 3, 7], 'Person_23': [7, 4, 10, 7, 9], 'Person_24': [5, 9, 4, 8, 3],
     'Person_25': [1, 7, 10, 6, 5], 'Person_26': [5, 0, 3, 2, 10], 'Person_27': [9, 3, 6, 3, 8],
     'Person_28': [10, 7, 7, 8, 1], 'Person_29': [0, 5, 6, 3, 2], 'Person_30': [8, 2, 4, 3, 2],
     'Person_31': [9, 6, 9, 10, 4], 'Person_32': [1, 2, 7, 7, 8], 'Person_33': [5, 1, 5, 7, 3],
     'Person_34': [0, 3, 6, 8, 4], 'Person_35': [9, 0, 2, 0, 3], 'Person_36': [4, 3, 3, 4, 8],
     'Person_37': [2, 9, 2, 9, 8], 'Person_38': [5, 4, 1, 3, 5], 'Person_39': [5, 5, 3, 8, 6],
     'Person_40': [9, 3, 7, 0, 0]}

# Tìm những người có 3/5 đầu điểm > 5.

list_x = []
for ten, diem in x.items() :
     data = {
          "v":ten,
          "s":diem
     }
     so = 0
     for so_diem in diem :
          if so_diem > 5:
               so += 1
               # print(so)
               if so == 3:
                    # print(so)
                    break
     if so == 3:
          list_x.append(data)
print(list_x)

