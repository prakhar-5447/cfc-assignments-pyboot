arr = [3,8,5,13,6,12,18,5]
for i in range (1,len(arr)-1):
    for j in range (0,len(arr)):
        if(arr[j]%2!=0):
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
print(arr)