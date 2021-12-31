import random
szam=int(input("Add meg mekkora a legnyagyobb dobható szám: "))
print()
i=1
f=1
while i == 1:
    randomszam = random.randint(1, szam)
    print("A számod:", randomszam)
    print()
    f=1
    while f == 1:
        ujra=input("Újra szeretnél dobni? Y/N: ")
        if ujra == "N" or ujra == "n":
            i=0
            f=0
            print("Program leáll")
        if ujra == "Y" or ujra == "y":
            f=0