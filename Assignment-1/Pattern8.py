# Print the following pattern:
#  *	*	*	*	*	*	*	*	*
#  *	*	*	*		*	*	*	*
#  *	*	*				*	*	*
#  *	*						*	*
#  * 								*
#  *	*						*	*
#  *	*	*				*	*	*
#  *	*	*	*		*	*	*	*
#  *	*	*	*	*	*	*	*	*

i = 1
k = 1
rows = 2 * 5 - 1
while(i<=rows):
    j=1
    col=1
    while(j<=rows):
        if (col<=5-k+1):
            print("*\t", end="")              
        else:
            print("\t", end="")
        if (j<5):
            col+=1
        else:
            col-=1         
        j+=1
    print("")
    if(i<5):
        k+=1          
    else:
        k-=1         
    i+=1