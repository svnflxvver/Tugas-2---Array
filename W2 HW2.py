"""Sebuah program digunakan untuk menyimpan dan menampilkan nama-nama klub yang
memenangkan pertandingan bola pada suatu grup pertandingan. Buatlah program yang
digunakan untuk merekap skor pertandingan bola 2 buah klub bola yang berlaga.

Pertama-tama program meminta masukan nama-nama klub yang bertanding, kemudian
program meminta masukan skor hasil pertandingan kedua klub tersebut. Yang disimpan dalam
array adalah nama-nama klub yang menang saja.

Proses input skor berhenti ketika skor salah satu atau kedua klub tidak valid (negatif).
Di akhir program, tampilkan daftar klub yang memenangkan pertandingan."""

A = input("Klub A : ")
B = input("Klub B : ")

count = 1
winner = []

print(f'Pertandingan {count}: ', end="")
skor = input().split()                                  #Array for storing input, comparison
if int(skor[0]) > int(skor[1]):
    winner.append(A)
elif int(skor[0]) < int(skor[1]):
    winner.append(B)
elif int(skor[0]) == int(skor[1]):
    winner.append('Draw')

while int(skor[0]) >= 0 and int(skor[1]) >= 0:
    count += 1
    print(f'Pertandingan {count}: ', end="")
    skor = input().split()                              #temporary list, reassignment
    if int(skor[0]) >= 0 and int(skor[1]) >= 0:         #in case negative, doesn't get stored to winner list
        if int(skor[0]) > int(skor[1]):
            winner.append(A)
        elif int(skor[0]) < int(skor[1]):
            winner.append(B)
        elif int(skor[0]) == int(skor[1]):
            winner.append('Draw')

winner_amt = len(winner)

for i in range(winner_amt):
    print(f"Hasil {i+1}: ",winner[i])
print("Pertandingan selesai")
