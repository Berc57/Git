import time

x = "."

f = open("szoveg.txt","r",encoding="utf-8")

szoveglista = []

for sor in f:
    szoveglista.append(sor.strip().split(";"))
    
print(szoveglista)

while x != "kilépés":
    x = input("-> ")
    if "szia" == x.lower():
        time.sleep(1)
        print(szoveglista[0][0])
    elif "helo"== x.lower():
        time.sleep(1)
        print(szoveglista[0][1])
    elif "jó" in x.lower():
        time.sleep(1)
        print(szoveglista[0][2])
    else:
        time.sleep(1)
        print("Tessék?")