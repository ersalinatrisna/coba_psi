nama=[]
gaji=[]
emas=[]
zakat=[]
pertahun=[]
perbulan=[]
nisab=[]
print ("+覧覧覧覧覧覧覧蘭+")
print ("| Penghitung Zakat Penghasilan |")
print ("| menurut pendapatan kasar (brutto) |")
print ("| |")
print ("+覧覧覧覧覧覧覧蘭+")
data=int(input("Masukan banyak data : "))
print("==========================================")

for i in range(data):
a = input(閃asukan nama : �)
nama.append(a)
b = int(input(閃asukan harga emas saat ini: �))
emas.append(b)
c = int(input(閃asukkan penghasilan Anda per bulan : �))
gaji.append(c)
print(�)

for i in range(data):
d = 12 * gaji[i]
pertahun.append(d)
e = 0.025 * pertahun[i]
zakat.append(e)
f = 85 * emas[i]
nisab.append(f)
g = zakat[i] / 12
perbulan.append(g)

for i in range(data):
print (�)
print(送覧覧覧覧覧覧-�)
print(� Zakat Penghasilan (Brutto)�)
print(送覧覧覧覧覧覧-�)
print(鮮ama :�,nama[i])
print(践arga 1 gram emas :�,坦p.�,emas[i])
print(善enghasilan per bulan :�,坦p.�,gaji[i])
print(善enghasilan per tahun :�,坦p.�,pertahun[i])
print(践arga nishab (85 gram emas) :�,坦p.�,nisab[i])
print(岨akat penghasilan :�,�2.5% x�,pertahun[i],�=�,坦p.�,zakat[i])
if pertahun[i] >= nisab[i]:
print(銭eterangan : WAJIB Zakat Rp.�,zakat[i],�/tahun�)
print(� atau Rp. �,perbulan[i],�/bulan�)
print(�)
if pertahun[i] <= nisab[i]:
print(銭eterangan : Anda belum termasuk Wajib Zakat�)
