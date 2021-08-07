# Print the following pattern:
#  5   5	5	5	5	5	5	5	5
#  5   4	4	4	4	4	4	4	5
#  5   4	3	3	3	3	3	4	5
#  5   4	3	2	2	2	3	4	5
#  5   4	3	2	1	2	3	4	5
#  5   4	3	2	2	2	3	4	5
#  5   4	3	3	3	3	3	4	5
#  5   4	4	4	4	4	4	4	5
#  5   5	5	5	5	5	5	5	5

i = 1
k=5
rows = 2*5-1
while(i<=rows):
    j=1
    col=5
    while(j<=rows):
        print(max(col,k),"\t", end="")
        if(j<5):
            col-=1
        else:
            col+=1
        j+=1
    if (i<5):
        k-=1
    else:
        k+=1
    print()
    i+=1