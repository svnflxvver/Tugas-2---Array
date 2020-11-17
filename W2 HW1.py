"""
Pos Pelayanan Terpadu (Posyandu) sebagai tempat pelayanan kesehatan perlu mencatat data berat balita (dalam kg). Petugas akan memasukkan data
tersebut kedalam array. Dari data yang diperoleh akan dicari berat balita terkecil, terbesar, dan reratanya.

"""
arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    sorted_berat = sorted(arrBerat)
    bMin = sorted_berat[0]
    bMax = sorted_berat[-1]
    return bMin,bMax


def rerata(arrBerat):
    total = 0.0
    # Definisikan Proses Mencari Rerata Dari Total Berat
    for i in arrBerat:
        total = total + i
    data_amt = len(arrBerat)
    avg = total / data_amt
    # Return Hasil Rerata
    return avg

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

Data_Berat = []
for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    Data_Berat = float(input())                           #Typecast ke float
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(Data_Berat)

# Panggil procedur hitungMinMax(arrBerat)
Minimum, Maximum = hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
average = rerata(arrBerat)
print("Berat balita minimum: {0:.2f}".format(float(Minimum)),"kg")
print("Berat balita maksimum: {0:.2f}".format(float(Maximum)),"kg")
print("Rerata berat balita: {0:.2f}".format(average),"kg")

