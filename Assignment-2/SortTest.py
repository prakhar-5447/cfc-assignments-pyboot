arr = [1,2,3,4,5,6,7,1]
count = 0
for i in range (1,len(arr)):
    if(arr[i - 1] > arr[i]):
        count += 1
        break
if count==1 :
    print("NOT SORTED")
else :
    print("SORTED")