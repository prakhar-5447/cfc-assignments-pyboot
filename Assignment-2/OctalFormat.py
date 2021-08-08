num = int(input("ENTER NUMBER : "))  
octal = 0
count = 1
while (num!=0) :
    rem = num % 8
    octal = octal + rem*count
    count = count * 10
    num = num // 8    
print(octal)