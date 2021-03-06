# -*- coding: utf-8 -*-
"""montecarlo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oL5Rm7frEwajF7A-_kYcICUeUDnoW0hy
"""

#Import Modul yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#Data Himpunan Awal
minta = [25, 35, 40, 45, 30, 55, 20, 15, 10, 50, 25, 55, 60, 30]

frequensi = np.random.randint(1, 25, size=14)

print(frequensi)

ngacak = []
interval = []
simulasi = []
untung = []

hari = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Himpunan distribusi kumulatif dengan nilai awal 0
kumulatif= [0]

#Deklarasi variabel awal
freqtot = 0
distp = 0
freqi = 0
dari=0
alpha = 43
c = 37
m = 61
nilais = 0
harga = 40000
modal = 20000
jadi = 0

#Fungsi untuk Menghitung Probabilitas
def kemungkinan(freq, n):
    return freq/n
    
#Fungsi untuk Menghitung angka acak dengan rumus
def angacak(x,a,c):
    return (x*a+c)
    
def mod(x,m):
    return x % m

#Fungsi untuk Mencari nilai dalam interval
def find(minta,kumulatif,interval,angka):
    for i in range(8):
        if (kumulatif[i] <= angka <=interval[i]):
            nilai = minta[i]
        else:
            pass
    return nilai

# Menghitung jumlah Frequensi
for i in range(len(frequensi)):
    freqtot += frequensi[i]
print(freqtot)

#Menghitung Distribusi Kemungkinan, Kumulatif dan Interval angka Acak
table1 = PrettyTable(['No', 'Permintaan/hari(kg)','Frekuensi','Distribusi Kemungkinan','Distribusi Kemungkinan Kumulatif'])
table2 = PrettyTable(['No', 'Permintaan/hari(kg)','Distribusi Kemungkinan','Distribusi Kemungkinan Kumulatif','Interval Angka'])
for i in range(len(minta)):
    dist = kemungkinan(frequensi[i], freqtot)
    distp += dist
    kum = round(distp, 2)
    sampai = int(kum*100)
    interval.append(sampai)
    table1.add_row([i+1,minta[i], frequensi[i], round(dist,2), kum])
    table2.add_row([i+1,minta[i], round(dist,2), kum, f'{kumulatif[i]} - {sampai}'])
    kumulatif.append(int(kum*100+1))
print(table1)
print('Total Frequensi =', freqtot)
print(table2)

#Menghitung Angka Acak
acak = np.random.randint(100)
ngacak.append(acak)

table3 = PrettyTable(['No', 'Xa+C mod M','Xi','Ui=Xi/M'])
for i in range(len(minta)):
    acak = angacak(ngacak[i],alpha,c)
    xi = mod(acak,m)
    ngacak.append(xi)
    u = round(xi / m,3)
    table3.add_row([i+1, acak, xi , u])
print(ngacak[0])
ngacak.pop(0)
print(table3)

table4 = PrettyTable(['No', 'Permintaan/hari(kg)','Interval Angka Acak','Bilangan Acak','Simulasi Permintaan'])
for i in range(len(minta)):
    nilai = find(minta,kumulatif,interval,ngacak[i])
    table4.add_row([i+1,minta[i], f'{kumulatif[i]}-{interval[i]}', ngacak[i], nilai])
    simulasi.append(nilai)
    nilais +=nilai
print(table4)
print('Total Permintaan =', nilais , 'kg')

#Memenghitung Keuntungan
table5 = PrettyTable(['No', 'Simulasi Permintaan','Keuntungan'])
for i in range(len(simulasi)):
    tk = simulasi[i] * harga - simulasi[i] * modal
    table5.add_row([i+1,simulasi[i], tk])
    untung.append(tk)
    jadi = jadi + tk
print(table5)
print('Total Keuntungan = Rp', jadi)

#Membuat Grafik Simulasi Permintaan
f = plt.figure(num='Grafik Simulasi Permintaan')
f = plt.plot(hari,simulasi, marker="o")
f = plt.xticks(np.arange(0, max(hari), 1))
f = plt.yticks(np.arange(0, max(simulasi)+20, 5))
f = plt.xlabel("Hari")
f = plt.ylabel("Kilogram")

#Membuat Grafik Simulasi Keuntungan
g = plt.figure(num='Grafik Simulasi Keuntungan')
g = plt.plot(hari,untung, marker="o")
f = plt.xticks(np.arange(0, max(hari), 1))
g = plt.yticks(np.arange(0, max(untung)+200000, 100000))
g = plt.xlabel("Hari")
g = plt.ylabel("Rupiah")

#Menampilkan Grafik
plt.show()