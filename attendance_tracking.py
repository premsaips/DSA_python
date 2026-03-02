#Attendance tracking system

#Dictionary to store attendance
attendance = {}

def show_menu():
    print("1.Add Attendance")
    print("2.View Attendance")
    print("3.exit")

def add_attendance():
    name = input("enter name of the student:")
    status = input("Enter status (present/absent)")
    attendance[name] = status
    print("Attendance add successfully")

def view_attendance():
    if not attendance:
        print("Attendance records not found..!")
        return()
    print("---- Attendance records ----")
    for name, status in attendance.items():
        print(f'{name} : {status}')
        

if __name__ == "__main__":
    print("== ATTENDANCE TRACKING SYSTEM ==")
    while True:
        show_menu()
        choice = int(input("enter you choice: "))
        if choice == 1:
            add_attendance()
        elif choice == 2:
            view_attendance()
        elif choice == 3:
            print("Thank you ...!")
            exit()
        else:
            print("invalid input")