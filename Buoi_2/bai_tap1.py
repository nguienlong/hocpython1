# # Tạo 1 list [5,3,4,0,6, 15, 18]
# # Lấy ra phần tử thứ 2.
# # Thêm phần tử 7 vào cuối
# # THêm phần tử 100 vào vị trị 1
# # THêm phần tử 100 vào vị trị 2
# # Xóa phần tử  5
# # Đếm phần tử 100 trong list
# # Lấy ra và xóa phần tử thứ 4.
# # Sắp xếp lại list
# # Clear list.
#
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


danh_sach = [0, 1 , 2, 3, 4, 5 ,6 , 7, 8, 9, 10 ]

try:
    # Cach lay danh sach tu phan tu thu 3 den phan tu thu 9
    print("Danh sach moi", danh_sach[3:9])
    # cach lay danh sach tu` phan tu thu 3 den het
    print("Danh sach moi", danh_sach[3:])
    print("Danh sach moi", danh_sach[3:len(danh_sach)])
    print("phan tu cuoi cach 1", danh_sach[len(danh_sach) - 1])
    print("Phan tu cuoi cach 2", danh_sach[-1])
    print("phan tu ngoai danh sach", danh_sach[13])
except Exception as ex:
    print("Loi:" , ex)
#
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

x = 1
y = 2
z = 3

# Dung va Dung: True
# Dung va Sai : False
# Sai va Sai: False

# Dung or sai: True
# Dung or dung : true
# Sai or Sai : False
danh_sach = [0 ,1 ,2 ,3, 4, 5, 6, 7, 8, 9, 10]
if x not in danh_sach:
    print("Khong co x trong danh sach")
else:
    print(" Co X trong danh sach")
if y in danh_sach:
    print("co y trong danh sach")
