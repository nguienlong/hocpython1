# 2) Lọc danh sách chuỗi
# 3) Lọc danh sách số thập phân
# 4)  Danh sách mới loại bỏ thành phần tử trùng lặp

#break : Ngat vong lap  for/ while
# Chu y: 1 break chi ngat for/ while thuoc lenh gan nhat

try:
    danh_sach = ["Mận","táo","Dưa","Táo","ổi","Mang Cụt",1,2,0.55,85,0.5,0.69,3,4,5,6,7,"Mang Cụt",
                 8,8,7,6,5,4,3,2,1,0.25,0.58,0.25,0.58,0.66,0.14,0.66,0.14,"Mận","táo","Dưa","Táo","ổi"]
    print("----->Danh Sách Lựa Chọn<------")
    print("1.Danh Sách Số Nguyên.")
    print("2.Danh Sách Chuỗi.")
    print("3.Danh Sách Số Thập Phân.")
    print("4.Danh Sách Mới Loại Bỏ Trùng Lặp.")
    lc = int(input("Mời Nhập Lựa Chọn : ",))

    if lc == 1:
        # 1) Lọc danh sách số tự nhiên#
        danh_sach_so_tu_nhien = []
        for phan_tu in danh_sach:
            if type(phan_tu) == int:
                danh_sach_so_tu_nhien.append(phan_tu)
        print(danh_sach_so_tu_nhien)
    elif lc == 2:
        # 2) Lọc danh sách chuỗi
        danh_sach_cach_chuoi = []
        for phan_tu in danh_sach :
            if type(phan_tu) == str :
                danh_sach_cach_chuoi.append(phan_tu)
        print(danh_sach_cach_chuoi)
    elif lc == 3:
        # 3) Lọc danh sách số thập phân
        danh_sach_so_thap_phan = []
        for phan_tu in danh_sach :
            if type(phan_tu) == float :
                danh_sach_so_thap_phan.append(phan_tu)
        print(danh_sach_so_thap_phan)
    elif lc == 4:
        # 4)  Danh sách mới loại bỏ thành phần tử trùng lặp
        danh_sach_khong_trung_lap = []
        for phan_tu in danh_sach:
            if phan_tu not in danh_sach_khong_trung_lap :
                danh_sach_khong_trung_lap.append(phan_tu)
        print(danh_sach_khong_trung_lap)
        # bien = list(set(danh_sach))
        # print(bien)
    else:
        print("chức năng không hợp lệ.")
except Exception as ex:
     print("Lỗi", ex)