arr = [1,2,3,4,5,11,11,11,11]
size = len(arr)
prime = [2,3,5,7]
count = 0
for i in range(0, size):
    if arr[i] == 2 or arr[i] == 3 or arr[i] == 5 or arr[i] == 7:
        count+=1
    if arr[i] > 1:
        if (arr[i] % 2) == 0:
            continue
        elif (arr[i] % 3) == 0:
            continue  
        elif (arr[i] % 5) == 0:
            continue
        elif (arr[i] % 7) == 0:
            continue
        else:
            count+=1
print("The count of prime numbers in array " , count)