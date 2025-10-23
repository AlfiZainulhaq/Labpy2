#input
bilangan1 = int(input("Masukan bilangan 1: ")) 
bilangan2 = int(input("Masukan bilangan 2: ")) 
bilangan3 = int(input("Masukan bilangan 3: ")) 
bilangan4 = int(input("Masukan bilangan 4: ")) 

#percabangan

terbesar = bilangan1

if bilangan2 > terbesar: 
    terbesar = bilangan2
    
if bilangan3 > terbesar:
    terbesar = bilangan3
    
if bilangan4 > terbesar:
    terbesar = bilangan4

#output
print (f"Bilangan terbesar adalah:: {terbesar}")