import time
import datetime
import random

ido = datetime.datetime.now()

x = "."

programdatum = 3
maidatum = int(ido.day)

r = "123"

f = open("szoveg.txt","r",encoding="utf-8")

szoveglista = []

for sor in f:
    szoveglista.append(sor.strip().split(";"))
    
print(szoveglista)

while x != "kilépés":
    x = input("-> ")
    if x.lower() == "kilépés":
        time.sleep(1)
        print("Viszlát!! Jó volt veled beszélgetni!!")
    elif "szia" in x.lower():
        time.sleep(1)
        print(szoveglista[0][0])
    elif "helo" in x.lower() or "hell" in x.lower():
        time.sleep(1)
        print(szoveglista[0][1])
    elif "jó" in x.lower():
        time.sleep(1)
        print(szoveglista[0][2])
    elif "idő" in x.lower():
        time.sleep(1)
        print(szoveglista[2][0]+str(ido.hour)+":"+str(ido.minute))
        print(ido.strftime("%A"))
    elif "dátum" in x.lower():
        time.sleep(1)
        print(szoveglista[2][1],str(ido.year)+"."+str(ido.month)+"."+str(ido.day)+".")
    elif "neved" in x.lower() or "hívnak" in x.lower():
        time.sleep(1)
        print(szoveglista[3][0])
        time.sleep(1)
        print(szoveglista[3][1])
        x = input("-> ")
        time.sleep(1)
        print(szoveglista[5][0])
    elif "ki vagy" in x.lower():
        time.sleep(1)
        print(szoveglista[3][0])
        time.sleep(1)
        print(szoveglista[4][2])
    elif "éves" in x.lower():
        time.sleep(1)
        print(szoveglista[4][0],int(maidatum)-int(programdatum),szoveglista[4][1])
    elif "programozott" in x.lower() or "programoztak" in x.lower():
        time.sleep(1)
        print(szoveglista[4][2])
    elif "köszi" in x.lower() or "köszönöm" in x.lower():
        time.sleep(1)
        print(szoveglista[5][2])
    elif "szívesen" in x.lower() or "szivesen" in x.lower():
        time.sleep(1)
        print(szoveglista[5][1])
    elif "számot" in x.lower():
        time.sleep(1)
        print(random.randint(0,1000000))
    elif "zene" in x.lower() or "zené" in x.lower():
        time.sleep(2)
        print(szoveglista[9][0])
        time.sleep(2)
        print(szoveglista[9][1])
        time.sleep(1.5)
        print(szoveglista[9][2])
        x = input("-> ")
        time.sleep(1)
        print(szoveglista[10][0])   
    elif "érzed" in x.lower():
        time.sleep(1)
        print(szoveglista[6][2])
        time.sleep(1)
        print(szoveglista[6][3])
        x = input("-> ")
        if "jól" in x.lower():
            time.sleep(1)
            print(szoveglista[7][1])
            time.sleep(1)
            print(szoveglista[7][2])
            x = input("-> ")
            time.sleep(1)
            print(":)")
        elif "rosszul" in x.lower():
            time.sleep(1)
            print(szoveglista[7][0])
            time.sleep(1)
            print(szoveglista[7][2])
            x = input("-> ")
            time.sleep(1)
            print(":(")
        else:
            time.sleep(2)
            print(szoveglista[8][1])
            time.sleep(1)
            print(szoveglista[7][3])
            x = input("-> ")
            if "jó" in x.lower():
                time.sleep(1)
                print(szoveglista[7][1])
                time.sleep(1)
                print(szoveglista[7][2])
                x = input("-> ")
                time.sleep(1)
                print(":)")
            elif "rossz" in x.lower():
                time.sleep(1)
                print(szoveglista[7][0])
                time.sleep(1)
                print(szoveglista[7][2])
                x = input("-> ")
                time.sleep(1)
                print(":(")
            else:
                time.sleep(1.5)
                print("Tessék?")
    elif "napod" in x.lower():
        time.sleep(1)
        print(szoveglista[6][0])
        time.sleep(1)
        print(szoveglista[6][1])
        x = input("-> ")
        if "jó" in x.lower():
            time.sleep(1)
            print(szoveglista[7][1])
            time.sleep(1)
            print(szoveglista[7][2])
            x = input("-> ")
            time.sleep(1)
            print(":)")
        elif "rossz" in x.lower():
            time.sleep(1)
            print(szoveglista[7][0])
            time.sleep(1)
            print(szoveglista[7][2])
            x = input("-> ")
            time.sleep(1)
            print(":(")
        else:
            time.sleep(2)
            print(szoveglista[8][0])
            time.sleep(1)
            print(szoveglista[7][3])
            x = input("-> ")
            if "jó" in x.lower():
                time.sleep(1)
                print(szoveglista[7][1])
                time.sleep(1)
                print(szoveglista[7][2])
                x = input("-> ")
                time.sleep(1)
                print(":)")
            elif "rossz" in x.lower():
                time.sleep(1)
                print(szoveglista[7][0])
                time.sleep(1)
                print(szoveglista[7][2])
                x = input("-> ")
                time.sleep(1)
                print(":(")
            else:
                time.sleep(1.5)
                print("Tessék?")
    elif "vicc" in x.lower():
        time.sleep(1)
        if str(random.choice(r)) == "1":
            print(szoveglista[11][0])
            time.sleep(1)
            x = input("-> ")
            time.sleep(2)
            print(szoveglista[11][1])
        elif str(random.choice(r)) == "2":
            print(szoveglista[11][2])
            time.sleep(1)
            x = input("-> ")
            time.sleep(2)
            print(szoveglista[11][3])
        elif str(random.choice(r)) == "3":
            print(szoveglista[11][4])
            time.sleep(1)
            x = input("-> ")
            time.sleep(2)
            print(szoveglista[11][5])
    elif "haha" in x.lower() or "xd" in x.lower():
        time.sleep(1)
        print(szoveglista[11][6])
    else:
        time.sleep(1.5)
        print("Tessék?")