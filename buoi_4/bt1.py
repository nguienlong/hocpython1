danh_sach_hoa_don = [{'Time': '08/05/2024', 'ban': 4, 'ghe': 11, 'tu': 19},
                     {'Time': '09/05/2024', 'ban': 1, 'ghe': 16, 'tu': 3},
                     {'Time': '10/05/2024', 'ban': 12, 'ghe': 18, 'tu': 13},
                     {'Time': '11/05/2024', 'ban': 12, 'ghe': 19, 'tu': 11},
                     {'Time': '12/04/2024', 'ban': 19, 'ghe': 12, 'tu': 16},
                     {'Time': '13/05/2024', 'ban': 18, 'ghe': 18, 'tu': 3},
                     {'Time': '14/05/2024', 'ban': 8, 'ghe': 14, 'tu': 19},
                     {'Time': '15/05/2024', 'ban': 19, 'ghe': 10, 'tu': 4},
                     {'Time': '16/05/2024', 'ban': 18, 'ghe': 18, 'tu': 14},
                     {'Time': '17/05/2024', 'ban': 9, 'ghe': 4, 'tu': 18},
                     {'Time': '18/05/2024', 'ban': 2, 'ghe': 2, 'tu': 18},
                     {'Time': '19/05/2024', 'ban': 18, 'ghe': 16, 'tu': 2},
                     {'Time': '20/05/2024', 'ban': 1, 'ghe': 7, 'tu': 14},
                     {'Time': '21/04/2024', 'ban': 1, 'ghe': 14, 'tu': 18},
                     {'Time': '22/05/2024', 'ban': 3, 'ghe': 20, 'tu': 6},
                     {'Time': '23/05/2024', 'ban': 6, 'ghe': 11, 'tu': 16},
                     {'Time': '24/05/2024', 'ban': 10, 'ghe': 20, 'tu': 2},
                     {'Time': '25/04/2024', 'ban': 16, 'ghe': 1, 'tu': 4},
                     {'Time': '26/05/2024', 'ban': 12, 'ghe': 17, 'tu': 14},
                     {'Time': '27/05/2024', 'ban': 11, 'ghe': 20, 'tu': 2}]


from datetime import datetime
#
ngay_hien_tai = datetime.now()
print(ngay_hien_tai)
print(ngay_hien_tai.year)
print(ngay_hien_tai.month)
print(ngay_hien_tai.day)
print(ngay_hien_tai.hour)
print(ngay_hien_tai.minute)
print(ngay_hien_tai.second)
print(ngay_hien_tai.microsecond)


#Hien thi tong so san pham ban nhieu nhat cua nhung ngay sau 20/5/2024
# date = '20/5/2024'
# date_time = datetime.strptime(date,"%d/%m/%Y")
#
# for hoa_don in danh_sach_hoa_don :
#     str_date = hoa_don['Time']
#     date_time_2 = datetime.strptime(str_date, "%d/%m/%Y")
#     if date_time_2 > date_time :
#         tong_so_san_pham = (hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
#         print(hoa_don['Time'],tong_so_san_pham)

#Hien thi tong so san pham ban nhieu min,max cua nhung ngay sau 20/5/2024
# #Cach 1:
# date = '20/5/2024'
# date_time = datetime.strptime(date,"%d/%m/%Y")
# list_tong_san_pham = []
# for hoa_don in danh_sach_hoa_don :
#     str_date = hoa_don['Time']
#     date_time_2 = datetime.strptime(str_date, "%d/%m/%Y")
#     if date_time_2 > date_time :
#         tong_so_san_pham = (hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
#         list_tong_san_pham.append(tong_so_san_pham)
# max_tong_so_san_pham = max(list_tong_san_pham)
# for hoa_don in danh_sach_hoa_don:
#     str_date = hoa_don['Time']
#     date_time_2 = datetime.strptime(str_date, "%d/%m/%Y")
#     if date_time_2 > date_time:
#         tong_so_san_pham = (hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
#         if tong_so_san_pham == max_tong_so_san_pham:
#             print(hoa_don['Time'], tong_so_san_pham)
#
# #Cach 2
# ngay_goc = '20/05/2024'
# ngay_gio = datetime.strptime(ngay_goc, "%d/%m/%Y")
# danh_sach_hoa_don_new = []
# for hoa_don in danh_sach_hoa_don:
#     ngay_tim = hoa_don['Time']
#     ngay_tim_datime = datetime.strptime(ngay_tim,"%d/%m/%Y")
#     if ngay_tim_datime > ngay_gio:
#         danh_sach_hoa_don_new.append(hoa_don)
#
# # # Cách 1: Tìm max thông qua list
# list_so_tu_ban = []
# for hoa_don in danh_sach_hoa_don_new:
#     list_so_tu_ban.append(hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])
# max_so_tu_ban = max(list_so_tu_ban)
# for hoa_don in danh_sach_hoa_don_new:
#     if hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'] == max_so_tu_ban:
#         print(hoa_don['Time'], ":", hoa_don['ban'] + hoa_don['ghe'] + hoa_don['tu'])