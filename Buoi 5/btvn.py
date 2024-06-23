# lower() / upper() / split("")
# strip() / startswith()/ endswith() / find() / replace()

#

# # Ví dụ 1 người dùng:
# {
#     "tên": "Nguyễn Ngọc Cương",
#     "tuổi": 18,   # Tuyển nhân viên >= 18 tuổi
#     "địa chỉ": "HY", # Giới hạn chỉ chọn HN, HY, HD, QN, HP, LC, YB, BN, HB ( Còn nếu ngoài các tỉnh sau thì print
#                      # Không tuyển người ở {tỉnh nhập}
#
#     "giới tính": True, # True: nam, False: Nữ
#     "chiều cao": 171,   # Yêu cầu chiều cao > 160
#     "vị trí": "Nhân Viên",  # Giám đốc / Trưởng Phòng / Nhân Viên   # Chỉ có 1 giám đốc. Nếu đã có giám đốc thì
#     # không thể thêm user mới và print Đã có giám đốc
#     "tình trạng hôn nhân": False,  #True: đã kết hôn, False: chưa kết hôn.
#     "lương": 100,
#     "tài khoản": "cuong123",
#     "mật khẩu": "1234567"
# }

# Viết 1 chương trình:
# 1) Thêm User  ( Tối đa có 20 người, nếu đã đầy thì thông báo :" Đã đủ nhân viên")
# 2) Xem thông tin User ( Nhập input tên)
# 3) Danh sách các nhân viên ở tỉnh đã nhập ( Nhập input Tỉnh)
# 4) Tăng/ giảm lương người dùng : (Nhập input tên để chọn người.)
# 5) Danh sách nhân viên có lương > số nhập Input
# 6) Hiển thị tổng lương phải trả hàng tháng cho mọi người
# 7) Hiển thị tổng số tiền phải trả trong 1 năm cho mọi người
# 8) Hiển thị tổng lương phải trả hàng tháng cho Nhân Viên
# 9) Hiển thị tổng lương phải trả hàng tháng cho Trưởng Phòng
# 10) Hiển thị số nhân viên nam, số nhân viên nữ.
# 11) 9 Thoát
#
import json

with open("btvnnnn.json", "r") as f:
   user = json.load(f)

while True:
    print("1) Thêm User")
    print("2) Xem thông tin User")
    print("3) Danh sách các nhân viên ở tỉnh đã nhập")
    print("4) Tăng/ giảm lương người dùng")
    print("5) Danh sách nhân viên có lương")
    print("6) Hiển thị tổng lương phải trả hàng tháng cho mọi người")
    print("7) Hiển thị tổng số tiền phải trả trong 1 năm cho mọi người")
    print("8) Hiển thị tổng lương phải trả hàng tháng cho Nhân Viên")
    print("9) Hiển thị tổng lương phải trả hàng tháng cho Trưởng Phòng")
    print("10) Hiển thị số nhân viên nam, số nhân viên nữ.")
    print("11) Thoát")

    lc = int(input("Lựa Chọn: "))
    # 1) Thêm User  ( Tối đa có 20 người, nếu đã đầy thì thông báo :" Đã đủ nhân viên")
    if lc == 1:
        ten = input('Tên :').lower()

        tuoi = int(input('Tuổi: '))
        if tuoi >= 18:
            pass
        else:
            print("Chỉ tuyển nhân viên >= 18 tuổi.")
            break
        print("NƠI BẠN ĐANG SINH SỐNG")
        dc = str(input('Địa chỉ: ')).upper()
        ds_dc = ["HN", "HY", "HD", "QN", "HP", "LC", "YB", "BN", "HB"]
        if dc not in ds_dc:
            print("Không tuyển người ở tỉnh: ", dc)
        gioi_tinh = input('Giới tính (nam/nữ): ')
        if gioi_tinh == 'nam':
            print(True)
        else:
            print(False)
        print("Chiều cao yêu cầu trên 160cm")
        chieu_cao = int(input('Chiều cao: '))
        if chieu_cao > 160:
            print("Đạt yêu cầu")
        else:
            print("Chiều cao yêu cầu > 160cm")
            break
        print("Vị trí mong muốn ứng tuyển: Giám đốc / Trưởng Phòng / Nhân Viên ")
        vi_tri = str(input('Vị trí mong muốn: '))
        ds_vc = ["Giám đốc", "Trưởng Phòng", "Nhân Viên"]
        # for vt in ds_vc:

        hon_nhan = input('Tình trạng hôn nhân(đã kết hôn/độc thân): ')
        if hon_nhan == 'đã kết hôn':
            print(True)
        else:
            print(False)
        luong = int(input('Lương: '))
        tk = input('Tên Đăng Nhập: ')
        mk = input('Mật Khẩu: ')
        new_user = {
            'Tên' : ten,
            'Tuổi' : tuoi,
            'Địa chỉ' : dc,
            'Giới tính' : gioi_tinh,
            'Chiều cao' : chieu_cao,
            'Vị Trí' : vi_tri,
            'Tình trạng hôn nhân' : hon_nhan,
            'Lương' : luong,
            'Tên Đăng Nhập' : tk,
            'Mật Khẩu' : mk,
        }
        user.append(new_user)
        with open("btvnnnn.json", "w") as f:
            json.dump(user, f, indent=4)
            break
    # 2) Xem thông tin User ( Nhập input tên)
    elif lc == 2:
        information = input("Tên người dùng cần xem thông tin: ")
        for inforuser in user:
            if inforuser['Tên'] == information:
                print("Thông Tin Nhân Viên là : " , inforuser)
                break
        else:
            print("Không có thông tin trong công ty")
        break
    # 3) Danh sách các nhân viên ở tỉnh đã nhập ( Nhập input Tỉnh)
    elif lc == 3:
        list_locations = input("Danh sách các nhân viên ở tỉnh đã nhập: ")
        for location in user:
            if location['Địa chỉ'] == list_locations:
                print("Những người thuộc tỉnh đã lọc là: " , location['Tên'])
        break
    # 4) Tăng/ giảm lương người dùng : (Nhập input tên để chọn người.)
    elif lc == 4:
        information_wage = input("Tên người dùng muốn tìm: ")
        for wage in user:
            if wage['Tên'] == information_wage:
                sua_luong = int(input("Số tiền cần sửa: "))
                wage['Lương'] = sua_luong
                print("Lương hiện tại của ",wage['Tên'], "là: ", wage['Lương'] )
                with open("btvnnnn.json", "w") as f:
                    json.dump(user, f, indent=4)
                break
        else:
            print("Không có thông tin trong công ty")
        break
    # 5) Danh sách nhân viên có lương > số nhập Input
    elif lc == 5:
        list_wage = int(input("Danh sách nhận viên có lương hơn hơn số nhập: "))
        for wage2 in user:
            if wage2['Lương'] > list_wage:
                print("Danh sách những người được lọc là: ", wage2['Tên'] )
        break
    # 6) Hiển thị tổng lương phải trả hàng tháng cho mọi người
    elif lc == 6:
        tong_luong_thang = 0
        for luong_thang in user:
            tong_luong_thang += luong_thang['Lương']
        print("Tổng lương hàng tháng phải trả là: ",tong_luong_thang )
        break
    # 7) Hiển thị tổng số tiền phải trả trong 1 năm cho mọi người
    elif lc == 7:
        tong_luong_thang = 0
        tong_luong_nam = 0
        for luong_thang in user:
            tong_luong_thang += luong_thang['Lương']
            tong_luong_nam = tong_luong_thang*12
        print("Tổng lương hàng năm phải trả là: ",tong_luong_nam)
        break
    # 8) Hiển thị tổng lương phải trả hàng tháng cho Nhân Viên
    elif lc == 8:
        tong_luong_thang_nv = 0
        for luong_thang_nv in user:
            if luong_thang_nv['Vị Trí'] == 'Nhân Viên':
                tong_luong_thang_nv += luong_thang_nv['Lương']
        print("Tổng lương của Nhân Viên là: ", tong_luong_thang_nv)
        break
    # 9) Hiển thị tổng lương phải trả hàng tháng cho Trưởng Phòng
    elif lc == 9:
        tong_luong_thang_tp = 0
        for luong_thang_tp in user:
            if luong_thang_tp['Vị Trí'] == 'Nhân Viên':
                tong_luong_thang_tp += luong_thang_tp['Lương']
        print("Tổng lương của Trưởng Phòng là: ", tong_luong_thang_tp)
        break
    # 10) Hiển thị số nhân viên nam, số nhân viên nữ.
    elif lc == 10:
        print("1.Số nhân viên nam trong công ty ")
        print("2.Số nhân viên nữ trong công ty ")
        nv = int(input("Lựa Chọn: "))
        if nv == 1:
            for nv_nam in user:
                if nv_nam["Giới tính"] == 'nam':
                    print( "Số nhân viên nam trong công ty là: ",nv_nam)
            break

        if nv == 2:
            for nv_nu in user:
                if nv_nu["Giới tính"] == 'nữ':
                    print( "Số nhân viên nam trong công ty là: ",nv_nu)
            break
    elif lc == 11:
        print("thoát")
        break
    else:
        print("Nhập Sai Số nhập lại")










