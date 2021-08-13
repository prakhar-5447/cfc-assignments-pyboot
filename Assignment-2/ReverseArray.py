arr = [22,42,75,1,24,20,15,17,4]
reverse = len(arr)//2
for i in range(0,reverse):
    temp=arr[i]
    arr[i]=arr[len(arr)-1-i]
    arr[len(arr)-1-i]=temp
    print(arr)
print(arr)
