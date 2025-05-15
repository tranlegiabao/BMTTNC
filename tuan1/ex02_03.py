#nhập só từ người dùng
so =  int(input("nhập 1 số tài nguyên"))
#kiểm tra xe số đó có phải số chẵn hay không
if so % 2 == 0:
    print(so, "là số chăn.")
else:
    print(so, "không phải là số chẵn.")