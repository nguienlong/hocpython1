# var_dict = {
#     "key": "value",
#     "abcd": 5
}
# # Sửa/ thêm value của key bất kì var_dict[key] = value
# var_dict["abcd"] = "value_2"
# print(var_dict)

# # #Lấy value của key:  var_dict[key]
# print(var_dict["abcd"])

#  Lấy 1 list key của var_dict
# print(var_dict.keys())
# # # lấy 1 list value của var_dict
# # print(var_dict.values())
# # lấy value của key, nhưng an toàn hơn  var_dict[key]
# # print(var_dict.get("thong_tin_3_ae", "khong_co"))
# # Lấy ra value của key và xóa cặp key-value khỏi dict
# # x = var_dict.pop("abcde")
# # Lấy và xóa phần tử ở cuối dict
# # var_dict.popitem()
# # Biến var_dict thành 1 dict trống
# # var_dict.clear()
# # giống list, tạo  dict mới giống dict cũ.
# # x = var_dict.copy()
# # lấy ra 1 list các list [key, value]
# # print(var_dict.items())
# # for phan_tu in var_dict.items():
# # Cập nhật dict cũ theo dict mới: trùng key thì thay đổi value ( value theo dict_2), không có thì thêm mới.
# # var_dict_2 = {"key": 5, "key1": 6}
# # var_dict.update(var_dict_2)
# print(var_dict)

# # Gán key mặc định value mới nếu chưa có. CÒn nếu trong dict có thì để nguyên
# var_dict.setdefault("thong_tin_2_ae", "abc")
# print(var_dict.pop())
# print(var_dict)
