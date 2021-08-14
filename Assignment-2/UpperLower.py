def uplow(self):
    if ch > 'A' and ch < 'Z' :
        print("UPPERCASE")
    elif ch > 'a' and ch < 'z' :
        print("LOWERCASE")
    else :
        print("WRONG KEY PRESS")


ch = input("ENTER ALPHABET : ")
uplow(ch)
