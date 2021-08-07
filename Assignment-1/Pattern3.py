# Print the following pattern:
#                   1
#               1   2	1
#           1	2   3	2   1
#       1   2	3   4   3   2	1
#   1 	2   3	4   5	4   3	2   1

i=1
while(i<=5):
    space=1
    j=1
    while(space<=5-i):
        print("\t", end="")
        space=space+1
    col=1
    while(j<=2*i-1):
        print(col,"\t", end="")
        j+=1
        if (j<=i):
            col+=1
                
        else:
            col-=1  
    print()
    i+=1
