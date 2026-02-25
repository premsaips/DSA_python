def check_grade(m):
    if m > 90:
        return "O+ Grade."
    elif m < 90 and m > 80:
        return 'A+ grade'
    elif m < 80 and m > 70:
        return 'A Grade.'
    elif m < 70 and m > 60:
        return "B grade."
    elif m < 60 and m > 50:
        return "C Grade."
    elif m < 50 and m > 40:
        return 'D Grade.'
    elif m < 40  and m > 35:
        return "E Grade."
    else:
        return 'fail'

def main():
    marks = int(input("enter Marks: "))
    print(check_grade(marks))