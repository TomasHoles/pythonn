def porovnani(num1,num2):
    if num1 > num2:
        print("Cislo {0} > {1}".format( num1,num2))
    else:
        print("Cislo {1} > {0}".format(num1,num2))


jmeno = input("Zadej svoje jmeno: ")
prijmeni = input("Zadej svoje prijmeni: ")

print("Tve jmeno je",jmeno,prijmeni)

cislo1 = input("Zadej prvni cislo:")
cislo2 = input("Zadej druhe cislo:")

porovnani(cislo1,cislo2)

