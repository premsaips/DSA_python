def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

def main():
    s = input("enter a string: ")
    print("vowels count: ",count_vowels(s))

main()