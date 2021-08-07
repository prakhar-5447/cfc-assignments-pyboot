#Print the following pattern:
#   *				                	*
#   *   *			                *	*
#   *   *   *		            *   *	*
#   *   *   *	*           *	*   *	*
#   *   *   *	*   *	*   *	*   *	*
#   *   *   *	*	        *	*   *	*
#   *   *   *			        *   *	*
#   *   *			                *	*
#   *					                *

i = 1
k = 1
rows = 2 * 5 - 1
cols = 2 * 5
while (i <= rows):
    j = 1
    col = 1
    while (j <= cols):
        if (col <= k):
            print("*\t", end="")
        else:
            print("\t", end="")
        if (j < 5):
            col+=1 
        if (j > 5):
            col-=1
        j+=1
    print()
    if (i < 5):
        k+=1
    else:
        k-=1
    i+=1
