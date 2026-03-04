def count_freq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

def main():
    arr = [1,2,2,1]
    print("Frequency: ",count_freq(arr))

main()
