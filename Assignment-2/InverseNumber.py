num = int(input("ENTER NUMBER : "))
arr = []
arr1 = []
rem = 0
while True:  
    if (num!=0):
        rem = num%10
        num //= 10
        arr.insert(0,rem)
        arr1.insert(0,rem)
    else: 
        break
for i in range (0,len(arr)):
   index = arr[i]-1
   value = i+1
   arr1[index] = value
for i in arr1:
    print(i, end="")
print()