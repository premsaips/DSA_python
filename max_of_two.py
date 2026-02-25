#Maximum of two numbers
def max_of_two(num1, num2):
    if num1 > num2:
        return f"{num1} is maximum."
    return f'{num2} is Maximum.'

def main():
    num1 = int(input("enter 1st number"))
    num2 = int(input("enter 2nd number"))
    print(max_of_two(num1,num2))

main()