# # print("bai 1")
# var = input("bai 1:")
# var = var +1
#
# print(var)

# x = int(input("x= :"))
# #
# y = int(input("y= :" ))
#
# print("Hieu 2 so la :", x - y)
# # if (dieu kien)
# x = ""
# y = "abc"
# z = x + y
# print("z", z)
# var = True
# if z:
#     print("Dung")
# else:
#     print("sai")
#
# x = 0
# y = 5
#
# # tinh tong, so sanh
# Tong= x + y
# print("Tong cua Tong =", Tong)
# if Tong > 0:
#     print("Dung")
# else :
#     print("sai")
# # tinh hieu, so sanh
# hieu= x - y
# print("hieu cua hieu =", hieu)
# if hieu > 0:
#     print("hieu dung")
# elif hieu == 0:
#     print("=0")
# else :
#     print("hieu sai")
# # tinh thuong, so sanh
# thuong = x  / y
# print("thuong cua z=", thuong)
# if thuong > 0:
#     print(" thuong dung")
# elif thuong == 0:
#     print("=0")
# else :
#     print("thuong sai")

# # Kieu du list: 1 danh sach chua cac bien nhu int, float, str, bool, list
#
# Bat dau tu 0 list_var[Vi tri Mong Muon]
# print("Phan tu thu 1:", list_var[1],list_var[3])
# Tim vi tri trong list: list_var.index(Gia tri can tim)
# print("Vi tri cua text:", list_var.index("text"),list_var.index(5.0))

# list.append(Gia Tri) : them gia tri cuoi cung` trong danh sach
# list_var.append(154)
# print(list_var)

# list.insert( vi tri, gia tri) vao list
# list_var.insert(1 ,0)
# print(list_var)

# list_var.count: Dem phan tu xuat hien trong hien trong list

# list_var.clear(): Xoa phan tu trong danh sach

# list_2 = list_var.copy():
# list_var.pop (vi tri) lay ra phan tu o vi tri duoc chon,xoa khoi list
# list_var = [1, "text", 5.0, True]
#
# print(list_var[1])
# list.remove( gia tri can xoa)

# x = list_var.pop(1)
# list.sort(reverse=False): sap xep list tang dan, list.sort(reverse=TRue): sap xep list Giam dan
# # danh_sach.sort(reverse=False)
# list_1 =[5,3,4]
# list_2 =[6,2,7]
# list_3 = list_1 + list_2
# print(list_3)
#
# # list_1.extend(list_3) # ~~ list_1 = list_1 + list_3
#
# list_3 = list_1*2
# print("list_1:", list_1)
# print("list_2:", list_2)
# print("list_3:", list_3)

# danh_sach = [5,8,6,4,2,10]
# print(danh_sach)
#
# input = input("Gia tri can nhap:")
# danh_sach.append(input)
# print(danh_sach)

# x = "buoi_tap_1"
#
# list_str = list(x) # bien string thang list
# print(list_str)
# list_str.remove('1')
# print(list_str)
# list_str.append('2')
# print(list_str)
#
# # "text".join(LIST): chen text vao giua cac phan tu trong list va xuat hien string. co the chuoi rong, khac  rong.
# var = "".join(list_str)
# print(var)
#
# y = "buoi_tap_1"
#
# list_str = list(y)
# print(list_str)
# list_str.insert(0,'python')
# print(list_str)
# var = "".join(list_str)
# print(var)
#
#
# list_str = list(var)
# print(list_str)
# x = list_str.index('n')+1
# print(x)
#
# list_str.insert(6,'_')
# print(list_str)
# var = "".join(list_str)
# print(var)

# for : vong lap qua danh sach, qua thanh tu minh muon thuc hien han hdong minh yeu cau.




# Variable in LIST -> True/False
# flag = "gsdaaz" in list_var
# if flag:
#     print("co a trong danh sach")
# else:
#     print("khong co a trong danh sach")


# list_var = [1, 0, 2, 3, 4, 5 , 9, 40, 8, 4]
# for item in list_var:
# #    neu phan tu > 5 thi` print phan tu do
#     if item > 5:
#         print(item)
#     elif item == 5:
#         print(item)
#     else:
#         print(item)

# list_tien_ban = [100, 57, 83, 77, 66 , 45, 78, 84, 62]
# # list_tien_lai = []
# # gia_goc = 50
# # for var in list_tien_ban:
# #     so_can_them = var - gia_goc
# #     list_tien_lai.append(so_can_them)
# #
# # print(list_tien_ban)
# # print(list_tien_lai)
# # print(sum(list_tien_lai))
#
# for index in range (0, 9):
#     print(list_tien_ban[index])
#     print(index)
# list_var = [5,3,4,0,6,15,18]
# print(list_var)
# print("tim ra phan tu 2:", list_var[2])
#
# print("them phan tu 7 vao cuoi.")
# list_var.append(7)
# print(list_var)
#
# print("them phan tu 100 vao vi tri 1.")
# list_var.insert(1,100)
# print(list_var)
# print("them phan tu 100 vao vi tri 2.")
# list_var.insert(2,100)
# print(list_var)
#
# print("xoa phan tu thu 5.")
# list_var.remove(5)
# print(list_var)
#
# print("dem phan tu 100 trong danh sach")
# list_var.count(100)
# print(list_var)
#
#
# print("Lấy ra và xóa phần tử thứ 4:",list_var.pop(4))
# print(list_var)
#
# print("Sắp xếp lại list tang dan`:")
# list_var.sort(reverse=False)
# print(list_var)
# print("Sắp xếp lại list giam dan`:")
# list_var.sort(reverse=True)
# print(list_var)
#
# print("Clear list")
# list_var.clear()
# print(list_var)
# print("oke")

# try:
#     pass
# except  Exception as ex:
#     print("Loi", ex)

# bien_fales = False
# bien_None = None
# ben_true = True
#
# if ben_true:
#     print(ben_true, "True")
# else:
#     print(ben_true, "False")
#
# if bien_fales :
#     print(bien_fales, "True")
# else:
#     print(bien_fales, "False")
# if bien_None :
#     print(bien_None, "True")
# else:
#     print(bien_None,"False")