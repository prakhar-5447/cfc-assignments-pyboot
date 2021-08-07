print("Enter two numbers")
num1 = int(input("Enter first numbers: "))
num2 = int(input("Enter seond numbers: "))
Num = num1
Deno = num2
while(Deno!=0):
    temp = Num % Deno
    Num = Deno
    Deno = temp
print("GCD of and  is" ,Num)