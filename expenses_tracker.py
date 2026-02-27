expenses = []

def show_men():
    print("Expenses tracker")
    print("1. Add expenses")
    print("2. view expenses")
    print("3. exit")

def add_expenses():
    name = input("enter expenses name: ")
    try:
        amount = float(input("enter amount: "))
    except ValueError:
        print("Invalid amount! please enter correct amount.")
        return
    expense = {
        'name': name,
        'amount':amount
    }
    expenses.append(expense)
    print("expense added successfully")

def view_expenses():
    if not expenses:
        print("No expenses found")
        return
    print("-------- EXPENSES LIST --------")
    total = 0
    for expense in expenses:
        print(f'{expense['name']} : {expense['amount']}')
        total += expense['amount']
    print("Total expenses are: ", total)

def main():
    while True:
        show_men()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("exiting thank you...!")
            exit()
        else:
            print("enter valid choice....!")
if __name__ == "__main__":
    main()