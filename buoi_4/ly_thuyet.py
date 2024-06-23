#------------ WHILE------------

# Tạo 1 list chứa phần tử số từ 1 đến 100 dùng for

# list = []
# for phan_tu in range (1,101):
#     list.append(phan_tu)
# print(list)

# Nếu giờ 3h30p
# print("Den gio dung chuong trinh")
# so = 1
# while True:
#     so += 1
#     if so == 101:
#         print(so)
#         break
#
# #cách 2
# while so < 101:
#     print(so)
import os

import pygame
from datetime import datetime

# Khởi tạo pygame
pygame.init()

file_name = "123.mp3"
while True:
    gio = input("Gio: ")
    phut = input("Phut: ")
    print(f"{gio} {phut}")
    date = datetime.now()
    hen_gio_date = f"{date.year}/{date.month}/{date.day} {gio}:{phut}"
    hen_gio_date_time = datetime.strptime(hen_gio_date, "%Y/%m/%d %H:%M")
    if hen_gio_date_time < date:
        print("Mời nhập lại!")
    else:
        break
while True:
    date = datetime.now()
    date_time = datetime.strftime(date, "%H:%M")
    if date_time == hen_gio:
        print("Dậy Thôi Ông Cháu ơi")

        # Đường dẫn đến file âm thanh (đường dẫn tuyệt đối)
        file_goc = os.getcwd()
        sound_file = f"{file_goc}/{file_name}"
        # Phát âm thanh
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        # Đợi cho đến khi âm thanh kết thúc
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        break


