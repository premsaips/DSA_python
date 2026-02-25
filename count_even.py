# def count_even(n):
#     count = 0
#     temp = n
#     while temp != 0:
#         digit = temp % 10
#         if digit % 2 == 0:
#             count += 1
#         temp = temp // 10
#     return count

# def main():
#     n = int(input('enter a number'))
#     print("Noof even numbers are: ", count_even(n))

# main()



def count_even2(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            count += i
    return count

def main():
    n = int(input("enter n value: "))
    print(f"Even count up to {n} is: {count_even2(n)}")

main()
