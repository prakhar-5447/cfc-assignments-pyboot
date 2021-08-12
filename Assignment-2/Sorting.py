arr = [0,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0]
for i in range(len(arr) - 1):
    min = i
    for j in range( i + 1, len(arr)):
        if(arr[j] < arr[min]):
            min = j
    if(min != i):
        arr[i], arr[min] = arr[min], arr[i]
print(arr)