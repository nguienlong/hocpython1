def validate_ten():
    while True:
        try:
            ten = str(input("tên: ")).lower()
            so = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            ki_tu_so = [str(item) for item in so]
            special_characters = [
                '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
                '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
            ki_tu = ki_tu_so + special_characters
            flag = False
            for ki_tu_chu_cai in ki_tu:
                if ki_tu_chu_cai in ten:
                    flag = True
                    print("nhap lai")
            if flag is False:
                return ten
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
            print("---------------------------------")

x = validate_ten()
print(x)