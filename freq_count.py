def duplicates(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for key,val in freq.items():
        if val > 1:
            print(key)
arr = [1,2,2,1,2,1,3,4]
duplicates(arr)