# Tạo một danh sách rỗng để lưu kểt quả
j=[]
# duyệt qua tất cả các số từ 2000 đén 3200, kiểm tra xem i có chia hết cho 7 và không phải là một số của 5 không
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print (','.join(j))