# def start_pat(n):
#     for i in range(1, n+1):
#         for j in range(1, i + 1):
#             print('*', end='')
#         print()

def start_pat(n):
    for i in range(n):
        for j in range(n):
            if i < j:
                print(" ", end='')
            else:
                print('*', end='')
        print()

def main():
    n = int(input("enter noof lines: "))
    start_pat(n)

main()


