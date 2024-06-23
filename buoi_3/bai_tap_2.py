# var_dict = {'An': 25, 'Binh': 30, 'Cuong': 28, 'Dung': 22, 'Hai': 35, 'Hoa': 20, 'Hung': 45, 'Khanh': 18, 'Lan': 40,
#             'Linh': 15, 'Mai': 32, 'Minh': 50, 'Nam': 27, 'Nga': 33, 'Nhan': 55, 'Phong': 38, 'Quan': 42, 'Quyen': 23,
#             'Son': 11, 'Tam': 47, 'Thang': 36, 'Thanh': 29, 'Thao': 16, 'Thuy': 52, 'Tung': 21, 'Tuyen': 58,
#             'Tuyet': 14, 'Van': 26, 'Vy': 34, 'Xuan': 19, 'Yen': 37, 'Khoa': 44, 'Khuong': 49, 'Lam': 24, 'Le': 31,
#             'Long': 39, 'My': 56, 'Nghia': 53, 'Nhung': 9}
#
# # Lấy ra tuổi của "An", "Minh", "Nam"
#
# # print("Tuoi Cua An:", var_dict['An'])
# #
# # print("Tuoi Cua Minh:", var_dict['Minh'])
# #
# # print("Tuoi Cua Nam:", var_dict['Nam'])
# #
# # # Thêm 1 cặp  Tên: tuổi mới chưa có trong dict
# # var_dict["Sam"] = "100"
# #
# # # Sửa tuổi của 'Van' là 10
# # var_dict["Van"] = 10
# #
# # # Lấy ra tuổi của 'Thang', nếu không có thì trả ra 10.
# # print(var_dict.get('Thang', 10))
# #
# # # Xóa thông tin của 'Nga' ra khỏi dict
# # var_dict.pop('Nga')
# # print(var_dict)
# # # Tạo 1 var_new mới bằng var_dict
# # var_new = var_dict.copy()
# # print(var_new)
# #
# # # Clear var_new
# # var_new.clear()
# # print(var_new)
# # # Sử dụng Setdefault cho 'Thuan' có tuổi là 50.
# # var_dict.setdefault('Thuan', 50)
# # print(var_dict)
# # # Sử dụng update với dict khác là:
# # var_dict_2 = {'Vy': 34, 'XuanHinh': 18, 'Yen': 35, 'Khoa': 40, 'Khuong': 55}
# # var_dict.update(var_dict_2)
# # print(var_dict)
# # # In ra list key của dict var_dict.keys()
# # print(var_dict.keys())
# # for phan_tu in var_dict.keys():
# #     print(phan_tu)
# # # In ra list value của dict
# # for phan_tu in var_dict.values():
# #     print(phan_tu)
# # print(var_dict_2.values())
# # # In ra list key-value của dict
# # for ten,tuoi in var_dict.items():
# #     print(ten,tuoi)
# # -----------------------------------------------------------
# danh_sach_nguoi = []
# # Tạo 1 list mới gồm những người 0- 20 tuổi
# for ten, tuoi in var_dict.items():
#     data = {
#             "ten": ten,
#             "tuoi": tuoi
#         }
#     if tuoi >= 0 and tuoi <= 20:
#         data["do_tuoi"] = "tre em"
#     elif tuoi >= 21 and tuoi <= 40:
#         data["do_tuoi"] = "nguoi lon"
#
#     else:
#         data["do_tuoi"] = "nguoi gia"
#     danh_sach_nguoi.append(data)
# print(danh_sach_nguoi)
#
# # Tạo 1 list mới gồm những người từ 21-40 tuổi
#
# # Tạo 1 list mới gồm những người từ 41-60 tuổi
#
# # ____________________________________________________________________________


x = {'Person_1': [10, 0, 5, 9, 4], 'Person_2': [7, 8, 2, 10, 3], 'Person_3': [0, 7, 0, 4, 6],
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

# Tìm những người có tổng điểm lớn hơn > 20, Tren 20 được học lực trung bình, trên 30 học lực khá, trên 40 học lực giỏi.
# #In ra danh sách những người đó format [{"Ten": ten, "Tong Diem": tong diem, "hoc_luc": hoc_loc}, {....}]

danh_sach = []
for ten, danh_sach_diem in x.items():
    tong_diem=sum(danh_sach_diem)
    data = {
        "Ten": ten,
        "Tong Diem":tong_diem ,
    }
    if tong_diem > 20:
        data["hoc_luc"] = "Trung Binh"
    elif tong_diem > 30 and tong_diem <= 40:
        data["hoc_luc"] = "Kha"
    else:
        data["hoc_luc"] = "Gioi"
    danh_sach.append(data)
print(danh_sach)
# Tìm những người có 3/5 đầu điểm > 5.

