# Print the following pattern: 
#  *
#  *   *
#  *   *   *
#  *   *   *   *
#  *   *   *   *    *

num = int(input("Enter number : "))
i=1
while(i<=num):
    j=1
    while(j<=i):
        print("*\t", end="")
        j+=1          
    print()
    i+=1