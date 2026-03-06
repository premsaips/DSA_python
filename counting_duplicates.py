def counting_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

def main():
    arr = [4,1,2,3]
    print("Are duplicates found: ", counting_duplicates(arr))

main()