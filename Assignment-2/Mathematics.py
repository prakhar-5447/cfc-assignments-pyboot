num1 = int(input("ENTER FIRST NUMBER : "))  
num2 = int(input("ENTER SECOND NUMBER : "))  
ch = (input("""ENTER
'+' For Addition
'-' For Substraction
'*' For Multiplication
'/' For Division
'%' For Modulus
"""))  

if ch == "+" :
    result = num1+num2
elif ch == "-" :
    result = num1-num2
elif ch == "*" :
    result = num1*num2
elif ch == "/" :
    result = num1/num2
elif ch == "%" :
    result = num1%num2
else :
    print("WRONG KEY PRESS")
    exit
print(result)