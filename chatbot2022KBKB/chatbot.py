import time

x = "."

f = open("szoveg.txt","r",encoding="utf-8")
while x != "kilépés":
    x = input("->")
    if "szia" == x:
        time.sleep(1)
        print("Neked is szia!!")
    elif "helo" == x:
        time.sleep(1)
        print("Helló")
    else:
        time.sleep(1)
        print("Tessék?")
