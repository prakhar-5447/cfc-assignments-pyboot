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

i = 1
k = 1
while(i<=5):
    sp = 1
    while(sp<=5-k):
        print("\t", end="")
        sp+=1            
    j = 1
    while(j<=2*k-1):
        print("*\t", end="")
        j+=1          
    if(i<5):
        k+=1          
    else:
        k-=1         
    print()
    i+=1
