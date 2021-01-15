teori = float(input("Nilai Ujian Teori: "))
praktek = float(input("Nilai Ujian Praktek: "))

if teori >= 70 and praktek >= 70:
 print("Selamat, anda lulus!")
elif teori >= 70 and praktek < 70:
 print("Anda harus mengulang ujian praktek.")
elif teori < 70 and praktek >= 70:
 print("Anda harus mengulang ujian teori.")
else:
 print("Anda harus mengulang ujian teori dan praktek.")