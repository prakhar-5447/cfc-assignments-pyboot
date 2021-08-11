arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    value = int(input())
    arr.append(value)
size = len(arr)
count = 0
for i in range(0,size):
    if(arr[i]%5 == 0):
        count+=1
print("The count of multiples in array " , count)