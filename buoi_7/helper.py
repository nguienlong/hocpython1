import json
import uuid
from datetime import datetime


# ver 1
def dang_ky(user: str, password: str):
    result = {
        "user": user,
        "password": password,
        "id": str(uuid.uuid4()),
        "time": datetime.now()
    }

    return result


# ver 2
def dang_ky_v2():
    list_user = []
    user = input("nhap user:")
    password = input("nhap password:")
    result = {
        "user": user,
        "password": password,
        "id": str(uuid.uuid4()),
        "time": datetime.now()
    }
    list_user.append(result)
    return "Đăngkysy thanh cong"


def hien_thi_so_nv():
    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    chucvu = input("Số Nhân Viên(GD,TP,NV: ").upper()
    so_nhan_nv = len([chuc_vu2 for chuc_vu2 in users if chuc_vu2['chuc_vu'] == 'nhân viên'])
    so_nhan_tp = len([chuc_vu2 for chuc_vu2 in users if chuc_vu2['chuc_vu'] == 'trưởng phòng'])
    so_nhan_gd = len([chuc_vu2 for chuc_vu2 in users if chuc_vu2['chuc_vu'] == 'giám đốc'])
    if chucvu == "NV":
        ket_qua = f"Số nhân viên: {so_nhan_nv}"
    elif chucvu == "TP":
        ket_qua = f"Số trưởng phòng: {so_nhan_tp}"
    elif chucvu == "GD":
        ket_qua = f"Số giám đốc: {so_nhan_gd}"
    else:
        ket_qua = f"Chức năng không hợp lệ"
    return ket_qua


def tim_dia_chia(dia_chi: str):
    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    list_result = []
    for user in users:
        if user['address'] == dia_chi:
            list_result.append({
                "user_name": user['name'],
                "dia_chi": user['address']
            })
    return list_result


def hien_thi_gioi_tinh(gioi_tinh: int):
    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    so_nhan_vien_nam = len([gioi_tinh for gioi_tinh in users if gioi_tinh['gender'] == 'nam'])
    so_nhan_vien_nu = len(users) - so_nhan_vien_nam

    if gioi_tinh == 1:
        ket_qua = so_nhan_vien_nam
    else:
        ket_qua = so_nhan_vien_nu
    return ket_qua


def xoa_nhan_vien_ban_muon(xoa_nv):
    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    flag = False
    for nguoi_dung in users:
        if nguoi_dung['chuc_vu'] == xoa_nv:
            vi_tri = users.index(nguoi_dung)
            users.pop(vi_tri)
            flag = True
            print("Đã Xóa Thành Công")
            break
    if flag is False:
        print("Không Thể Xóa không tìm thấy người dùng")

    return users


def sua_email(email: str, user: dict):

    duoi_emails = ['@gmail.com', '@yahoo.com', '@hotmail.com']
    flag = False
    for duoi_email in duoi_emails:
        if email.endswith(duoi_email) and len(email) > len(duoi_email):
            flag = True
            user['email'] = email
            break

    if flag is True:
        result = {
            "da_sua": 1,
            "data": user
        }
    else:
        result = {
            "da_sua": 0,
            "data": user
        }
    return result


def sua_ngay_sinh(ngay_sinh: str, user: dict):
    try:
        check = datetime.strptime(ngay_sinh, "%d/%m/%Y")
        date_now = datetime.now()
        sotuoi = int(date_now.year) - int(check.year)
        user['birthday_date'] = ngay_sinh
        if sotuoi > 18:
            result = {
                "da_sua": 1,
                "data": user,
            }
        else:
            result = {
                "da_sua": 0,
                "data": user
            }
    except:
        result = {
            "da_sua": 0,
            "data": user
        }
    return result

def sua_password(matkhau: str, user:dict):
    user['pass'] = matkhau
    if len(matkhau) >= 8:
        result = {
            "da_sua": 1,
            "data": user,
        }
    else:
        result = {
            "da_sua": 0,
            "data": user
        }
    return result

def sua_ten(name: str, user: dict):
    user['name'] = name
    result = {
        "name": name,
        "data": user,
    }
    return result

def sua_phone_number(phone_number: str, user: dict):
    if len(phone_number) != 10:
        result = {
            "da_sua": 0,
            "data": user
        }
        return result
    flag = True
    for number in phone_number:
        if number not in '0123456789':
            flag = False
            break
    if flag is True:
        user['phone_number'] = phone_number
        result = {
            "da_sua": 1,
            "data": user
        }
    else:
        result = {
            "da_sua": 0,
            "data": user
        }
    return result

def sua_gioi_tinh(gender: str,user: dict ):
    user['gender'] = gender
    result = {
        "gender": gender,
        "data": user,
    }
    return result

def sua_dia_chi(address: str,user: dict ):
    user['address'] = address
    result = {
        "address": address,
        "data": address,
    }
    return result

def sua_chuc_vu(chuc_vu: str, user: dict ):
    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    user['chuc_vu'] = chuc_vu
    if chuc_vu == "giám đốc":
        flag_chuc_vu = False
        for user in users:
            if user["chuc_vu"].lower() == "giám đốc":
                flag_chuc_vu = True
                user['chuc_vu'] = chuc_vu
                break
        if flag_chuc_vu is False:
            result = {
                "da_sua": 1,
                "data": user
            }
        else:
            result = {
                "da_sua": 0,
                "data": user
            }
        return result

# def tim_thong_tin_nv():






