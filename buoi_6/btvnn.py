import uuid
import json
from datetime import datetime
with open("baitapvnn.json", "r") as f:
    user = json.load(f)

# user = []
while True:
    print("______________________________________________")
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Sua thong tin nhan vien")
    print("4. Xoa nhan vien")
    print("5. Danh sách các nhân viên ở tỉnh")
    print("6. Hiển thị số nhân viên nam/nữ.")
    print("7. Hiển thị số nhân viên có chuc vu")
    lc = int(input("Lựa Chọn Chức Năng: "))
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
# Số lượng user tối đa 20,  chỉ 1 giám đốc, tuổi > 18
#     print("1. Thêm User")
#     print("2. Xem thông tin User")
#     print("3. Sua thong tin nhan vien")
#     print("4. Xoa nhan vien")
#     print("5. Danh sách các nhân viên ở tỉnh:")
#     print("6. Hiển thị số nhân viên nam/nữ.")
#     print("7. Hiển thị số nhân viên có chuc vu (input)") # GD, TP, NV
#     print("8. Thoát")
    if lc == 1:
        if len(user) == 20:
            print("Đã đủ nhân viên")
            continue

        user_id = str(uuid.uuid4())

        duoi_emails = ["@gmail.com", "@yahoo.com"]
        email = input("Mời nhập email: ")
        flag = False
        for duoi_email in duoi_emails:
            if email.endswith(duoi_email) and len(email) > len(duoi_email):
                flag = True
                break
        if flag is False:
            print("Email không hợp lệ")
            continue
        birth_day = input("Nhập ngày tháng năm sinh(dd/mm/yy):")
        try:
            kiemtra = datetime.strptime(birth_day, "%d/%m/%Y")
            date_now = datetime.now()
            sotuoi = int(date_now.year) - int(kiemtra.year)
            if sotuoi < 18:
                print("Chưa Đủ Tuổi Đi làm")
                break
        except:
            print("Ngày tháng Không Hợp lệ")
            break
        password = input("Mời nhập mật khẩu: ")
        if len(password) < 8:
            print("Mật khẩu không hợp lệ")
            continue
        name = str(input("Mời nhập tên thật: ")).lower()
        phone_number = input("Mời nhập số điện thoại: ")
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
        address = input("Địa chỉ: ")
        gender = "nam"
        if gender not in  ["nam", "nu"]:
            print("Giới tính không hợp lệ")
        chuc_vus = input("Mời nhập chức vụ: ").lower()
        if chuc_vus == "giám đốc":
            flag_chuc_vu = False
            for cv in user:
                if cv["chuc_vu"] == "giám đốc":
                    flag_chuc_vu = True
                    break
            if flag_chuc_vu is False:
                print("Đã có giám đốc")
                continue
        date = datetime.now()
        ngay_tao = f"{date.day}/{date.month}/{date.year} {date.hour}:{date.minute}"
        print("Ngày tạo user: ",ngay_tao )
        new_user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "birthday_date": birth_day,
            "pass": password,  # Tren 8 ky tu
            "name": name,
            "phone_number": phone_number,
            "address": address,
            "gender": gender,
            "chuc_vu": chuc_vus,
            "ngay_tao": ngay_tao,

        }
        user.append(new_user)
        with open("baitapvnn.json", "w") as f:
            json.dump(user, f, indent=4)
            break
# 2) Xem thông tin User ( Nhập input tên)
    elif lc == 2:
        information = input("Tên người dùng cần xem thông tin: ")
        for infor in user:
            if infor["name"] == information:
                print("Thông Tin Nhân Viên là : ", infor)
                break
        else:
            print("Không có thông tin trong công ty")
        break
# 3) Sua thong tin nhan vien"
    elif lc == 3:
        sua_thong_tin_user = input("Tên người dùng muốn tìm: ")
        for thong_tin_user in user:
            if thong_tin_user['name'] == sua_thong_tin_user:
                print("------Mời nhập chức năng------")
                print("1. Sửa email")
                print("2. Sửa ngày sinh")
                print("3. Sửa mật khẩu")
                print("4. Sửa tên")
                print("5. Sửa sđt")
                print("6. Sửa địa chỉ")
                print("7. Sửa giới tính")
                print("8. Sửa chức vụ")
                sua = int(input("Lựa Chọn Chức Năng: "))
                if sua == 1:
                    duoi_emails = ["@gmail.com", "@yahoo.com"]
                    email = input("mail cần sửal: ")
                    flag = False
                    for duoi_email in duoi_emails:
                        if email.endswith(duoi_email) and len(email) > len(duoi_email):
                            flag = True
                            thong_tin_user['email'] = email
                            with open("baitapvnn.json", "w") as f:
                                json.dump(user, f, indent=4)
                            break
                    if flag is False:
                        print("Email không hợp lệ")
                        continue
                elif sua == 2:
                    birth_day = input("Nhập ngày tháng năm sinh(dd/mm/yy):")
                    try:
                        kiemtra = datetime.strptime(birth_day, "%d/%m/%Y")
                        date_now = datetime.now()
                        sotuoi = int(date_now.year) - int(kiemtra.year)
                        if sotuoi < 18:
                            print("Chưa Đủ Tuổi Đi làm")
                            break
                        else:
                            thong_tin_user['birthday_date'] = birth_day
                            with open("baitapvnn.json", "w") as f:
                                json.dump(user, f, indent=4)
                    except:
                        print("Ngày tháng Không Hợp lệ")
                        break
                elif sua == 3:
                    password = input("Mời nhập mật khẩu: ")
                    if len(password) < 8:
                        print("Mật khẩu không hợp lệ")
                        break
                    else:
                        thong_tin_user['pass'] = password
                        with open("baitapvnn.json", "w") as f:
                            json.dump(user, f, indent=4)
                        continue
                elif sua == 4:
                    if thong_tin_user['name'] == sua_thong_tin_user:
                        sua_ten = input("Tên cần sửa: ")
                        thong_tin_user['name'] = sua_ten
                        with open("baitapvnn.json", "w") as f:
                            json.dump(user, f, indent=4)
                        continue
                elif sua == 5:
                    phone_number = input("Mời nhập số điện thoại: ")
                    if len(phone_number) != 10:
                        print("Số điện thoại không hợp lệ")
                    flag = True
                    for number in phone_number:
                        if number not in '0123456789':
                            flag = False
                        else:
                            thong_tin_user['phone_number'] = phone_number
                            with open("baitapvnn.json", "w") as f:
                                json.dump(user, f, indent=4)
                            break
                    if flag is False:
                        print("Sđt không hợp lệ")
                        continue
                elif sua == 6:
                    sua_dia_chi = input("Địa chỉ cần sửa: ")
                    thong_tin_user['address'] = sua_dia_chi
                    with open("baitapvnn.json", "w") as f:
                        json.dump(user, f, indent=4)
                    continue
                elif sua == 7:
                    gender = input("giới tính muốn sửa: ")
                    if gender not in ["nam", "nu"]:
                        print("Giới tính không hợp lệ")
                    else:
                        thong_tin_user['gender'] = gender
                        with open("baitapvnn.json", "w") as f:
                            json.dump(user, f, indent=4)
                elif sua == 8:
                    chuc_vus = input("Mời nhập chức vụ: ").lower()
                    if chuc_vus == "giám đốc":
                        flag_chuc_vu = False
                        for thong_tin_user in user:
                            if thong_tin_user["chuc_vu"] == "giám đốc":
                                flag_chuc_vu = True
                                thong_tin_user['chuc_vu'] = chuc_vus
                                with open("baitapvnn.json", "w") as f:
                                    json.dump(user, f, indent=4)
                                break
                        if flag_chuc_vu is False:
                            print("Đã có giám đốc")
                            continue
    elif lc == 4:
        xoa_thong_tin = input("Tên người dùng muốn tìm: ")
        flag = False
        for xoa_tt in user:
            if xoa_tt['chuc_vu'] == xoa_thong_tin:
                user.pop(user.index(xoa_tt))
                flag = True
                print("đã xóa thành công")
                with open("baitapvnn.json", "w") as f:
                    json.dump(user, f, indent=4)
                continue
        if flag is False:
            print("Không Thấy người dùng")
        continue
    elif lc == 5:
        dia_chi = input("Danh sách các nhân viên ở tỉnh ")
        for tinh_nv in user:
            if tinh_nv['address'] == dia_chi:
                print("người ở tỉnh",dia_chi,"là",user)
        break
    elif lc == 6:
        print("1.Số Nhân Viên Nam     2. Số Nhân Viên Nữ")
        gioi_tinh = int(input("Số Nhân Viên: "))
        so_nhan_vien_nam = len([gioi_tinh for gioi_tinh in user if gioi_tinh['giới tính'] == 'Nam'])
        so_nhan_vien_nu = len(user) - so_nhan_vien_nam
        if gioi_tinh == 1:
            print(so_nhan_vien_nam)
        else:
            print(so_nhan_vien_nu)
        break

    elif lc == 7:
        chucvu = input("Hiển thị số nhân viên có chuc vu")
        so_nv = len([chuc_vu for chuc_vu in user if chuc_vu['chuc_vu'] == 'nhân viên'])
        so_tp = len([chuc_vu for chuc_vu in user if chuc_vu['chuc_vu'] == 'trưởng phòng'])
        so_gd = len([chuc_vu for chuc_vu in user if chuc_vu['chuc_vu'] == 'nhân viên'])
        if chucvu == "NV":
            print(so_nv)
        elif chucvu == "TP":
            print(so_tp)
        else:
            print(so_gd)

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