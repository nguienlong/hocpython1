import uuid
import json
import os
from datetime import datetime


from buoi_7.helper import tim_dia_chia, hien_thi_so_nv, hien_thi_gioi_tinh, xoa_nhan_vien_ban_muon, sua_email, \
    sua_ngay_sinh, sua_password, sua_ten, sua_phone_number, sua_gioi_tinh, sua_dia_chi, sua_chuc_vu

with open("baitapvn.json", "r") as f:
    users = json.load(f)
# users = []
while True:
    print("----------------------------------------------------------------------")
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Sua thong tin nhan vien")
    print("4. Xoa nhan vien")
    print("5. Danh sách các nhân viên ở tỉnh")
    print("6. Hiển thị số nhân viên nam/nữ.")
    print("7. Hiển thị số nhân viên có chuc vu")
    print("8. Thoát")
    lua_chon = int(input("Lựa Chọn Chức Năng: "))

    if lua_chon == 1:
        if len(users) == 20:
            print("Đã đủ nhân viên")
            continue
        email = input("email: ")
        duoi_emails = ['@gmail.com', '@yahoo.com', '@hotmail.com']
        flag = False
        for duoi_email in duoi_emails:
            if email.endswith(duoi_email) and len(email) > len(duoi_email):
                flag = True
                break
        if flag is False:
            print("Email không hợp lệ")
            continue
        ngay_sinh = input("Nhập Ngày Sinh(dd/mm/yy): ")
        try:
            check = datetime.strptime(ngay_sinh, "%d/%m/%Y")
            date_now = datetime.now()
            sotuoi = int(date_now.year) - int(check.year)
        except:
            print("Ngày tháng không hợp lệ")
            continue

        mat_khau = input("Nhập Mật Khẩu: ")
        if len(mat_khau) < 8:
            print("mật khẩu phải lớn hơn 8 ký tự")
            continue
        name = str(input("Họ Và Tên: ")).lower()

        phone_number = input("Số Điện Thoại: ")
        if len(phone_number) != 10:
            print("Số điện thoại không hợp lệ")
            continue
        flag = True
        for number in phone_number:
            if number not in '0123456789':
                flag = False
                break
        if flag is False:
            print("Sđt không hợp lệ")
            continue
        address = input("Địa chỉ: ")

        genderr = input("Giới Tính: ").lower()
        if genderr not in ['nam', 'nữ']:
            print("giới tính Không Hợp Lệ")
            continue
        chuc_vu = input("Chức Vụ CV: ").lower()
        if chuc_vu == "giám đốc":
            flag_chuc_vu = False
            for user in users:
                if user["chuc_vu"].lower() == "giám đốc":
                    flag_chuc_vu = True
                    break
            if flag_chuc_vu is True:
                print("Đã có giám đốc")
                continue
        date = datetime.now()
        datetimes = f"{date.hour}:{date.minute} {date.day}/{date.month}/{date.year}"
        user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "birthday_date": ngay_sinh,
            "pass": mat_khau,  # Tren 8 ky tu
            "name": name,
            "phone_number": phone_number,
            "address": address,
            "gender": genderr,
            "chuc_vu": chuc_vu,
            "ngay_tao": datetimes
        }
        users.append(user)
        with open("baitapvn.json", "w") as f:
            json.dump(users, f, indent=4)
        continue

    elif lua_chon == 2:
        nhap_user = input("Thông tin nhân viên muốn tìm: ").lower()
        flag = False
        for tim_user in users:
            if tim_user['id'] == nhap_user:
                flag = True
                print(tim_user)
        if flag is False:
            print("Không Có Thông Tin Nhân Viên")
            continue
    elif lua_chon == 3:
        sua_user = input("Nhập Thông Tin Muốn Sửa: ").lower()
        for user in users:
            sua_user = input("Nhập Thông Tin Muốn Sửa: ")
            print("-----------------Lựa chọn thông tin muốn sửa--------------------------")
            print("1.email  2.ngày sinh  3.mật khẩu  4.Họ Tên 5.số điện thoại 6.giới tính "
                  "7.nơi ở 8.chức vụ")
            sua_thongtin = int(input("Lựa Chọn Chức Năng: "))
            for user in users:
                if user['id'] == sua_user:
                    print(user)
                    if sua_thongtin == 1:
                        email = input("email: ")

                        result = sua_email(email=email, user=user)

                        if result['da_sua'] == 1:
                            user = result['data']
                            print("Đã sửa thành công")
                            with open("baitapvn.json", "w") as f:
                                json.dump(users, f, indent=4)
                        else:
                            print("Email không hợp lệ")

                        enter = input('Enter để tiếp tiếp tục chương trình')
                        continue

                if sua_thongtin == 2:
                    ngay_sinh = input("Nhập Ngày Sinh(dd/mm/yy): ")

                    result = sua_ngay_sinh(ngay_sinh=ngay_sinh, user=user)

                    if result['da_sua'] == 1:
                        user = result['data']
                        print("Đã sửa thành công")
                        with open("baitapvn.json", "w") as f:
                            json.dump(users, f, indent=4)
                    else:
                        print("Ngày sinh không hợp lệ")
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue
                if sua_thongtin == 3:
                    matkhau = input("Nhập Mật Khẩu Muốn Đổi: ")

                    result = sua_password(matkhau=matkhau, user=user)

                    if result['da_sua'] == 1:
                        user = result['data']
                        print("Đã sửa thành công")
                        with open("baitapvn.json", "w") as f:
                            json.dump(users, f, indent=4)
                    else:
                        print("Mật khẩu không đủ theo yêu cầu")
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue
                if sua_thongtin == 4:
                    name = input("Họ Tên Muốn Đổi: ").lower()

                    result = sua_ten(name=name, user=user)

                    user = result['data']
                    print("Đã sửa thành công")
                    with open("baitapvn.json", "w") as f:
                        json.dump(users, f, indent=4)
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue
                if sua_thongtin == 5:
                    phone_number = input("Số Điện Thoại: ")

                    result = sua_phone_number(phone_number=phone_number, user=user)

                    if result['da_sua'] == 1:
                        user = result['data']
                        print("Đã sửa thành công")
                        with open("baitapvn.json", "w") as f:
                            json.dump(users, f, indent=4)
                    else:
                        print("Số điện thoai")
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue

                if sua_thongtin == 6:
                    gender = input("Giới Tính Muốn Sửa: ")

                    result = sua_gioi_tinh(gender=gender, user=user)

                    user = result['data']
                    print("Đã sửa thành công")
                    with open("baitapvn.json", "w") as f:
                        json.dump(users, f, indent=4)
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue

                if sua_thongtin == 7:
                    address = input("Địa chỉ Muốn Sửa: ")

                    result = sua_dia_chi(address=address, user=user)

                    user = result['data']
                    print("Đã sửa thành công")
                    with open("baitapvn.json", "w") as f:
                        json.dump(users, f, indent=4)
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue

                if sua_thongtin == 8:
                    chuc_vu = input("Chức Vụ Muốn Thay: ").lower()

                    result = sua_chuc_vu(chuc_vu=chuc_vu, user=user)

                    if result['da_sua'] == 1:
                        user = result['data']
                        print("Đã sửa thành công")
                        with open("baitapvn.json", "w") as f:
                            json.dump(users, f, indent=4)
                    else:
                        print("Số điện thoai")
                    enter = input('Enter để tiếp tiếp tục chương trình')
                    continue
                with open("baitapvn.json", "w") as f:
                    json.dump(users, f, indent=4)
    elif lua_chon == 4:
        print("Bạn Có Chắc Chắn Mốn Xóa hết Nhân Viên....")
        xoa_nv = input("Nếu có thì nhập nhân viên: ")
        resutl = xoa_nhan_vien_ban_muon(xoa_nv=xoa_nv)
        with open("baitapvn.json", "w") as f:
            json.dump(resutl, f, indent=4)
    #     print("5. Danh sách các nhân viên ở tỉnh:")
    elif lua_chon == 5:
        dia_chi = input("Nhầm Tỉnh Muốn Tìm : ")
        # -> Hiển thị thêm các tỉnh có thể chọn.
        result = tim_dia_chia(dia_chi=dia_chi)
        if len(result) == 0:
            print("không nhân viên nào ở tỉnh trên")
        else:
            for tt in result:
                print(tt)
        continue

    #     print("6. Hiển thị số nhân viên nam/nữ.")
    elif lua_chon == 6:
        print("1.Số Nhân Viên Nam     2. Số Nhân Viên Nữ")
        gioi_tinh = int(input("Số Nhân Viên: "))
        ket_qua = hien_thi_gioi_tinh(gioi_tinh=gioi_tinh)
        if gioi_tinh == 1:
            print("Số Nhân Viên Nam là :", ket_qua)
        else:
            print("Số Nhân Viên Nữ là :", ket_qua)
        continue

    #     print("7. Hiển thị số nhân viên có chuc vu (input)") # GD, TP, NV

    elif lua_chon == 7:
        result = hien_thi_so_nv()
        print(result)
        continue
    else:
        break