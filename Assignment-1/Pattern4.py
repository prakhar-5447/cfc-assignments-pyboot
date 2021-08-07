# Print the following pattern:
# 		            1
#	            2   3	2
#	        3	4   5	4   3
#       4   5	6   7	6   5	4
#   5   6   7	8   9	8   7	6   5

num = int(input("Enter number : "))
i=1
while(i<=num):
    sp = 1
    while(sp<=num-i):
        print("\t", end="")
        sp+=1
    j=1
    col=i
    while(j<=2*i-1):
        print(col,"\t", end="")
        j+=1
        if (j<=i):
            col+=1               
        else:
            col-=1           
    print()
    i+=1       