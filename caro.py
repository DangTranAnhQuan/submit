"""Đặng Trần Anh Quân 23110292"""
def tao_bang():
    return [[' ' for _ in range(15)] for _ in range(15)]

def hien_thi_bang(bang):
    print("   " + " ".join(str(i) for i in range(15)))
    for i, hang in enumerate(bang):
        print(f"{i:2d} " + " ".join(hang))
    print()

def kiem_tra_thang_hang(bang, dong, cot, quan_co):
    count = 0
    for i in range(cot, min(cot + 5, 15)):
        if bang[dong][i] == quan_co:
            count += 1
        else:
            break
    return count == 5

def kiem_tra_thang_cot(bang, dong, cot, quan_co):
    count = 0
    for i in range(dong, min(dong + 5, 15)):
        if bang[i][cot] == quan_co:
            count += 1
        else:
            break
    return count == 5

def kiem_tra_thang_cheo_trai(bang, dong, cot, quan_co):
    count = 0
    for i, j in zip(range(dong, min(dong + 5, 15)), range(cot, min(cot + 5, 15))):
        if bang[i][j] == quan_co:
            count += 1
        else:
            break
    return count == 5

def kiem_tra_thang_cheo_phai(bang, dong, cot, quan_co):
    count = 0
    for i, j in zip(range(dong, max(dong - 5, -1), -1), range(cot, min(cot + 5, 15))):
        if bang[i][j] == quan_co:
            count += 1
        else:
            break
    return count == 5

def kiem_tra_thang(bang, dong, cot, quan_co):
    return (
        kiem_tra_thang_hang(bang, dong, cot, quan_co) or
        kiem_tra_thang_cot(bang, dong, cot, quan_co) or
        kiem_tra_thang_cheo_trai(bang, dong, cot, quan_co) or
        kiem_tra_thang_cheo_phai(bang, dong, cot, quan_co)
    )

def choi_caro():
    bang = tao_bang()
    luot_choi = 'X'

    while True:
        hien_thi_bang(bang)

        dong = int(input(f"Nhập dòng cho {luot_choi} (0-14): "))
        cot = int(input(f"Nhập cột cho {luot_choi} (0-14): "))

        if 0 <= dong < 15 and 0 <= cot < 15 and bang[dong][cot] == ' ':
            bang[dong][cot] = luot_choi
            if kiem_tra_thang(bang, dong, cot, luot_choi):
                hien_thi_bang(bang)
                print(f"Người chơi {luot_choi} thắng!")
                break
            luot_choi = 'O' if luot_choi == 'X' else 'X'
        else:
            print("Vị trí không hợp lệ. Hãy chọn lại.")

if __name__ == "__main__":
    choi_caro()