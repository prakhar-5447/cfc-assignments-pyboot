"""
BEGIN
NUMBER n1 , n2 , gcd = 1, i
OUTPUT "Enter first Number:"
INPUT n1
OUTPUT "Enter second Number:"
INPUT n2
 FOR  i = 1; i <= n1 && i <= n2; ++i THEN
    
	IF n1 % i == 0 && n2 % i == 0 THEN
		gcd = i
        END IF
END FOR
OUTPUT " G.C.D of "+n1+"and "+n1+" is "+ gcd
END
"""

print("Enter two numbers")
num1 = int(input("Enter first numbers: "))
num2 = int(input("Enter seond numbers: "))
Num = num1
Deno = num2
while(Deno!=0):
    temp = Num % Deno
    Num = Deno
    Deno = temp
print("GCD of and  is" + Num)
