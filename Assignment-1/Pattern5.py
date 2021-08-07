#Print the following pattern:
# 1
# 1	 1
# 1	 2	1
# 1	 3	3	1
# 1	 4	6	4	1
# 1	 5	10	10	5	1

i=0
while(i<=5):
    j=0
    value = 1
    while(j<=i):
        print(int(value),"\t", end="")
        next = value * (i-j) / (j+1)
        value = next
        j+=1        
    print()
    i+=1
