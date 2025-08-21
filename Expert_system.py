# Hệ chuyên gia xem hôm nay có nên nấu ăn không

def expert_system(do_sieng_nang,tien_tk,thoi_tiet):
    #Máy suy luận
    if do_sieng_nang=="không oke":
        return "Bạn nên đi ăn ngoài cho khỏe"
    elif tien_tk<=100000:
        return "Bạn nên ăn ngoài cho tiết kiệm"
    elif thoi_tiet=="mưa" and tien_tk>=200000:
        return "Bạn nên đi nấu ăn cho tâm trạng tốt"
    else:
        return "Bạn nên đi nấu ăn đi"
print("hệ chuyên gia tư vấn có đi nấu ăn hay không: ")
do_sieng_nang = input("Độ siêng hôm nay của bạn thế nào (ok/không oke): ").lower()
tien_tk=int(input("Số tiền hôm nay của bạn thế nào"))
thoi_tiet=input("Hôm nay thời tiết thế nào nhỉ(mưa/nắng): ").lower()

print(expert_system(do_sieng_nang,tien_tk,thoi_tiet))
