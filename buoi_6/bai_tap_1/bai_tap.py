import uuid
import datetime

# Số lượng user tối đa 20,  chỉ 1 giám đốc, tuổi > 18



# {
#     "id": "abc",
#     "email": "....@email.com"
#     "birthday_date": "dd/mm/yy"
#
#     "pass": ........ # Tren 8 ky tu
#     "name ": "Nguyen Van A"
#     "phone_number ": "0123456789"
#     "address": "xa, huyen, tinh"
#     "gender" : "nam/nu"
#     "chuc_vu" : "........."
#     "ngay_tao" : "dd/mm/yy h-m-s"
# }

# Tạo id
# user_id = str(uuid.uuid4())

# # xác định email
# duoi_emails = ["@gmail.com", "@yahoo.com"]
#
# gmail = "@gmail.com"
#
# flag = False
# for duoi_email in duoi_emails:
#     if gmail.endswith(duoi_email) and len(gmail) > len(duoi_email):
#         flag = True
#         break
# if flag is False:
#     print("Email không hợp lệ")

# xác định sđt hợp lệ
# phone_number = "0a23456789"
#
# if len(phone_number) != 10:
#     print("Số điện thoại không hợp lệ")
#
#
# flag = True
# for number in phone_number:
#     if number not in '0123456789':
#         flag = False
#         break
# if flag is False:
#     print("Sđt không hợp lệ")


# gender = "nam"
# if gender not in  ["nam", "nu"]:
#     print("gioi tinh khong hop le")

while True:
    print("____________________________________________")
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Sua thong tin nhan vien")
    print("4. Xoa nhan vien")
    print("5. Danh sách các nhân viên ở tỉnh:")
    print("6. Hiển thị số nhân viên nam/nữ.")
    print("6. Hiển thị số nhân viên có chuc vu (input)") # GD, TP, NV
    print("7. Thoát")

    lc = int(input("Lựa Chọn Chức Năng: "))

    if lc == 1:

        user_id = str(uuid.uuid4())

        gmail = input("Moi ban nhap Gmail:")
        duoi_emails = ["@gmail.com", "@yahoo.com"]

        flag = False
        for duoi_email in duoi_emails:
            if gmail.endswith(duoi_email) and len(gmail) > len(duoi_email):
                flag = True
                break
        if flag is False:
            print("Email không hợp lệ")
            continue

        birth_j


        day = "Moi Nhap nay sinh: "

        mat_khau = int(input("Mat khau:" ))
        if mat_khau < 8:
            print("MK khong du 8 KY TU")

        ten = str(input("Tên: ")).upper()

        phone_number = input("Moi nhap sdt: ")
        if len(phone_number) != 10:
            print("Số điện thoại không hợp lệ")
        flag = True
        for number in phone_number:
            if number not in '0123456789':
                flag = False
                break
        if flag is False:
            print("Sđt không hợp lệ")
            continue

        address = str(input("Địa Chỉ: ")).upper()

        new_user = {
            "id": user_id,
            "gmail": gmail,
            "birthday" : birth_day,
            "pass" : mat_khau,
            "name": ten,
            "phone_number ": phone_number,
            # "address": address,
            # "gender" : gender,
            # "chuc_vu": chuc_vu,
            # "ngay_tao": ngay_tao

        }




