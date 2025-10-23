bil1 = int(input("Masukan bilangan 1: ")) 
bil2 = int(input("Masukan bilangan 2: ")) 
bil3 = int(input("Masukan bilangan 3: ")) 
bil4 = int(input("Masukan bilangan 4: ")) 

if str(bil1 > bil2 & bil1 > bil3 & bil1 > bil4):
    terbesar = bil1
elif str(bil2 > bil1 & bil2 > bil3 & bil2 > bil4):
    terbesar = bil2
elif str(bil3 > bil1 & bil3 > bil2 & bil3 > bil4):
    terbesar = bil3
else:
    terbesar = bil4

print ("Bilangan terbesar adalah:", terbesar)