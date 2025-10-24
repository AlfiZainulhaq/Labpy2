print("Program mengurutkan data (tanpa sort/sorted)")

# Input jumlah data
n = int(input("Masukkan jumlah data (min 3): "))

if n < 3:
    print("Jumlah data minimal 3!")
else:
    data = []
    for i in range(n):
        bil = int(input(f"Bilangan ke-{i+1}: "))
        data.append(bil)

    # Algoritma Bubble Sort
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                # Tukar posisi elemen
                data[j], data[j + 1] = data[j + 1], data[j]

    # Tampilkan hasil
    print("Urutan bilangan: ", *data)