danh_sach_hoa_don = [{'Time': '08/05/2024', 'ban': 4, 'ghe': 11, 'tu': 19},
                     {'Time': '09/05/2024', 'ban': 1, 'ghe': 16, 'tu': 3},
                     {'Time': '10/05/2024', 'ban': 12, 'ghe': 18, 'tu': 13},
                     {'Time': '11/05/2024', 'ban': 12, 'ghe': 19, 'tu': 11},
                     {'Time': '12/05/2024', 'ban': 19, 'ghe': 12, 'tu': 16},
                     {'Time': '13/05/2024', 'ban': 18, 'ghe': 18, 'tu': 3},
                     {'Time': '14/05/2024', 'ban': 8, 'ghe': 14, 'tu': 19},
                     {'Time': '15/05/2024', 'ban': 19, 'ghe': 10, 'tu': 4},
                     {'Time': '16/05/2024', 'ban': 18, 'ghe': 18, 'tu': 14},
                     {'Time': '17/05/2024', 'ban': 9, 'ghe': 4, 'tu': 18},
                     {'Time': '18/05/2024', 'ban': 2, 'ghe': 2, 'tu': 18},
                     {'Time': '19/05/2024', 'ban': 18, 'ghe': 16, 'tu': 2},
                     {'Time': '20/05/2024', 'ban': 1, 'ghe': 7, 'tu': 14},
                     {'Time': '21/05/2024', 'ban': 1, 'ghe': 14, 'tu': 18},
                     {'Time': '22/05/2024', 'ban': 3, 'ghe': 20, 'tu': 6},
                     {'Time': '23/05/2024', 'ban': 6, 'ghe': 11, 'tu': 16},
                     {'Time': '24/05/2024', 'ban': 10, 'ghe': 20, 'tu': 2},
                     {'Time': '25/07/2024', 'ban': 16, 'ghe': 1, 'tu': 4},
                     {'Time': '26/05/2024', 'ban': 12, 'ghe': 17, 'tu': 14},
                     {'Time': '27/05/2024', 'ban': 11, 'ghe': 20, 'tu': 2}]

# Dùng while in ra các hóa đơn theo ngày: ...

# Duyệt Phần tử trong 1 list theo while
vitri = 0
while vitri < len(danh_sach_hoa_don):
    phan_tu = danh_sach_hoa_don[vitri]

# bodyy code
    print(phan_tu)
# body code
    vitri += 1
# theo for
for phan_tu in danh_sach_hoa_don:
       print(phan_tu)