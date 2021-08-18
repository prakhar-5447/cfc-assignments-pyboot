arr1 = [3, 1, 11, 2, 9, 7, 4, 5, -1, 13, 6]
arr2 =[]
target = 8
for i in range (0,len(arr1)):
    for j in range (1,len(arr1)):
        if(arr1[i]+arr1[j]==target):
            arr2.append((arr1[i],arr1[j]))   
print(arr2)