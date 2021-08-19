def arr_subsets(arr, arr1=[], index = 0):
    if index > len(arr)-1:
        print(arr1)
        return
    arr1.append(arr[index])
    arr_subsets(arr, arr1, index+1)
    arr1.pop()
    arr_subsets(arr,arr1, index+1)
arr= [1,2,3]
arr_subsets(arr)