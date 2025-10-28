print ("Program mengurutkan data")

# Input data
a = int(input("Bilangan ke-1: "))
b = int(input("Bilangan ke-2: "))
c = int(input("Bilangan ke-3: "))
d = int(input("Bilangan ke-4: "))

# Membandingkan
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

# Tampilkan hasil
print("Urutan bilangan:", a, b, c, d)