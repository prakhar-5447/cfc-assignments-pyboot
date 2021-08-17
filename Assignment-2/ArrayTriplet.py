arr1 = [3, 1, 2, 9, 7, 5, -1, 6]
arr2 =[]
target = 9
for i in range (0,len(arr1)-2):
    for j in range (i+1,len(arr1)-1):
        for k in range (j+1,len(arr1)):
            if(arr1[i]+arr1[j]+arr1[k]==target):
                arr2.append((arr1[i],arr1[j],arr1[k]))   
print(arr2)