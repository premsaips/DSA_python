def two_pointer(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
arr = [2,7,11,13]
target = 9
print(two_pointer(arr,target))