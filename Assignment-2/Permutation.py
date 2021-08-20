def permutations(arr,index=0):
    if index >= len(arr):
        print(arr)
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]
        permutations(arr,index+1)
        arr[i], arr[index] = arr[index], arr[i]
arr=[7,2,6]        
permutations(arr)