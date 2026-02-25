def count_pos(numbers):
    count = 0
    for i in numbers:
        if i > 0:
            count += 1
    return count

def main():
    nums = [1,-2,-3,4,8,6,-1]
    print("positive count = ",count_pos(nums))

main()