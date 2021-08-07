#Print the following pattern:
#                   *
#	            *   *	*
#           *	*   *	*   *
#	    *   *	*   *	*   *	*
#   *	*   *	*   *	*   *	*   *
#	    *   *   *   *   *   *	*
#	        *	*   *	*   *
#	            *   *	*
#		            *

row = int(input("Enter number : "))
i = 1
k = 1
while(i<=row):
    sp = 1
    while(sp<=int(row/2)-k+1):
        print("\t", end="")
        sp+=1            
    j = 1
    while(j<=2*k-1):
        print("*\t", end="")
        j+=1          
    if(i<int(row/2)+1):
        k+=1          
    else:
        k-=1         
    print()
    i+=1