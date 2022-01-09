import random
szam=int(input("Add meg mekkora a legnyagyobb dobható szám: "))
print()
valasz=1
ujraker=1
while valasz == 1:
    randomszam = random.randint(1, szam)
    print("A számod:", randomszam)
    print()
    ujraker=1
    while ujraker == 1:
        ujra=input("Újra szeretnél dobni? Y/N: ")
        if ujra == "N" or ujra == "n":
            valasz=0
            ujraker=0
            print("Program leáll")
        if ujra == "Y" or ujra == "y":
            ujraker=0
