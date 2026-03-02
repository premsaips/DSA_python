def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n//2):
            if n % i ==0:
                return False
        return True
    
n = int(input("enter a value: "))
if is_prime(n):
    print("it is a prime number.")
else:
    print("Not a prime number")
