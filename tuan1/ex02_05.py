so_gio_lam = float(input("nhập số giờ làm:"))
luong_gio = float(input("nhap thù lao mỗi giò làm tiêu chuẩn: "))
gio_tieu_chuan = 44 
gio_vuot_chan = max(0, so_gio_lam - gio_tieu_chuan )
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chan * luong_gio * 1.5
print(f"số tiền thực lĩnh của nhân viên:{thuc_linh}")
