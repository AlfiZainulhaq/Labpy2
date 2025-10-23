a = int(input("Masukan bilangan 1: ")) 
b = int(input("Masukan bilangan 2: ")) 
c = int(input("Masukan bilangan 3: ")) 
d = int(input("Masukan bilangan 4: ")) 

if a > b:
    terbesar = a
elif b > c:
    terbesar = b
elif c > d:
    terbesar = c
else: 
    terbesar = d

print (f"Bilangan terbesar adalah:: {terbesar}")