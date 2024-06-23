
import json
from datetime import datetime
with open("user2.json", "r") as f:
    user = json.load(f)
# user = []
while True:
    print("---------Quản lý điểm sinh viên---------")
    print("1. Nhập thông tin sinh viên")
    print("2. Tính điểm trung bình của mỗi sinh viên")
    print("3. Hiển thị số học sinh giỏi/ khá / yếu")
    print("4. Hiển thị cơ cấu % học sinh yếu, khá, giỏi")
    print("5. Tìm số học sinh có số điểm > số nhập và môn học yêu cầu")


    lc = int(input("Lựa Chọn: "))

    if lc == 1:
        ten = str(input("Họ Và Tên: ")).lower()

        toan = float(input("Mời nhập điểm Toán: "))
        if toan < 0 or toan > 10:
            print("Nhập Sai: ")
            continue
        van = float(input("Mời nhập điểm Văn: "))
        if van < 0 or van > 10:
            print("Nhập Sai: ")
            continue
        li = float(input("Mời nhập điểm Lí: "))
        if li < 0 or li > 10:
            print("Nhập Sai: ")
            continue
        hoa = float(input("Mời nhập điểm Hóa: "))
        if hoa < 0 or hoa > 10:
            print("Nhập Sai: ")
            continue
        su = float(input("Mời nhập điểm Sử: "))
        if su < 0 or su > 10:
            print("Nhập Sai: ")
            continue
        dia = float(input("Mời nhập điểm Địa: "))
        if dia < 0 or dia > 10:
            print("Nhập Sai: ")
            continue
        my_thuat = float(input("Mời nhập điểm Mỹ Thuật: "))
        if my_thuat < 0 or my_thuat > 10:
            print("Nhập Sai: ")
            continue
        am_nhac = float(input("Mời nhập điểm Âm nhạc: "))
        if am_nhac < 0 or am_nhac > 10:
            print("Nhập Sai: ")
            continue
        tieng_anh = float(input("Mời nhập điểm Tiếng anh: "))
        if tieng_anh < 0 or tieng_anh > 10:
            print("Nhập Sai: ")
            continue
        data = {
            "ten": ten,
            "ds_mon_hoc": {
                "toan": toan,
                "van":van,
                "li": li,
                "hoa": hoa,
                "su": su,
                "dia": dia,
                "my_thuat": my_thuat,
                "am_nhac": am_nhac,
                "tieng_anh": tieng_anh,
            }
        }
        user.append(data)
        with open("user2.json", "w") as f:
            json.dump(user, f, indent=4)
    elif lc == 2:
        nhap_ten = str(input("Họ Và Tên muốn tính điểm trung bình : ")).lower()
        for ds_nhap_ten in user:
            if ds_nhap_ten['ten'] == nhap_ten:
                a = ds_nhap_ten.get("ds_mon_hoc")
                diem_trung_binh = (a["toan"] + a["van"]+a["li"]+a["van"]+a["hoa"]+a["su"]+a["dia"]+a["my_thuat"]+a["am_nhac"]+a["tieng_anh"]) / len(a)
                print("Điểm trung bình của", nhap_ten, "là:", diem_trung_binh)
                break
    elif lc == 3:
        gioi = 0
        kha = 0
        tb = 0
        for phanloai in user:
            a = phanloai.get("ds_mon_hoc")
            diem_trung_binh = (a["toan"] + a["van"]+a["li"]+a["van"]+a["hoa"]+a["su"]+a["dia"]+a["my_thuat"]+a["am_nhac"]+a["tieng_anh"]) / len(a)
            if diem_trung_binh >= 8:
                gioi += 1
            elif diem_trung_binh > 4 and diem_trung_binh <= 8:
                kha += 1
            else:
                tb += 1
        print("SỐ HỌC SINH GIỎI LÀ:",gioi)
        print("SỐ HỌC SINH KHÁ LÀ:",kha)
        print("SỐ HỌC SINH TRUNG BÌNH LÀ:",tb)
        break
    elif lc == 4:
        gioi = 0
        kha = 0
        tb = 0
        for phanloai in user:
            a = phanloai.get("ds_mon_hoc")
            diem_trung_binh = (a["toan"] + a["van"] + a["li"] + a["van"] + a["hoa"] + a["su"] + a["dia"] + a[
                "my_thuat"] + a["am_nhac"] + a["tieng_anh"]) / len(a)
            if diem_trung_binh >= 8:
                gioi += 1
            elif diem_trung_binh > 4 and diem_trung_binh <= 8:
                kha += 1
            else:
                tb += 1
        phan_tram_gioi = (gioi / (gioi+kha+tb))*100
        phan_tram_kha = (kha / (gioi+kha+tb))*100
        phan_tram_tb = (tb / (gioi+kha+tb))*100

        print("tỉ lệ % hsg là:",phan_tram_gioi ,"%")
        print("tỉ lệ % hsk là:",phan_tram_kha ,"%")
        print("tỉ lệ % hstb là:",phan_tram_tb ,"%")
        break
    elif lc == 5:
        mon_hoc = str(input("Nhập môn học : ")).lower()
        so_diem = float(input("Nhập số điểm:"))
        for tim in user:
            d = tim.get("ds_mon_hoc")
            for mon, diem in d.items():
                if diem > so_diem and mon == mon_hoc:
                    print("Tất cả thông tin học sinh có số điểm môn", mon_hoc, ">",so_diem, "là: ",tim )






















