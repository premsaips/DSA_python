def cal_fee(course,marks):
    course = course.strip().lower()
    if course == 'ai':
        fee = 40000

    elif course == 'web':
        fee = 45000

    elif course == 'data science':
        fee = 35000

    else:
        None

    #Apply discount

    if marks > 90:
        print("fees consession id 10000")
        print("Original fee", fee)
        fee -= 10000
        print("After applying discount fee is: ", fee)
    else:
        print("No fee consession.")
        print("fees after discount is:", fee)
    
def main():
    course = input("enter you course: [Ai/ data science/ web]")
    try:
        marks = int(input('enter your marks: '))

        if marks < 0 or marks > 100:
            print("Enter valid marks from 0 to 100")
            return
    except ValueError:
        print("Invalid value")
    cal_fee(course, marks)

main()

        


    
