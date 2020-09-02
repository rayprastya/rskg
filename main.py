import rskg

print("Pendaftaran Layanan Rumah Sakit")
print("Silahkan pilih layanan yang ingin digunakan")
print("1. Antrian Hemodialisa")
print("2. Antrian Poliklinik")
print("( Masukan angka nya saja )")

antrian=input()

run=rskg.rskgi(antrian)
run.login()
#run.ambil_antrian()
run.cek_kamar()