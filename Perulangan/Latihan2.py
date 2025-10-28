import random

n = int(input("Masukkan jumlah n: "))
count = 0

while count < n:
    x = random.random()
    if x < 0.5:
        print(x)
        count += 1