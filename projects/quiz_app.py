#Quiz app cli

#Questions list
questions = [{"question": "2 + 2", "answer": '4'},
             {"question": " Capital of india", "answer":"New delhi"}]

def save_score(name, score):
    with open("scoreboard.txt", "a") as file:
        file.write(name + ' - ' + str(score) + "\n")

def show_scoreboard():
    try:
        with open("scoreboard.txt", 'r') as file:
            print("----- SCORE BOARD -----")
            print(file.read())
    except FileExistsError:
        print("No Score yet.")
    
#Run quiz
def run_quiz():
    name = input("Enter your name: ")
    score = 0
    for q in questions:
        answer = input(q["question"]+ " ")
        if answer.lower() == q['answer'].lower():
            print("correct")
            score += 1
        else:
            print("Wrong answer")
    print("Final Score: ",score)
    save_score(name, score)

def main():
    while True:
        print("\n ------ QUIZ APP -----")
        print("1. Take Quiz")
        print("2. View Scoreboard")
        print("3. exit")

        choice = int(input("enter your choice"))

        if choice == 1:
            run_quiz()
        elif choice == 2:
            show_scoreboard()
        elif choice == 3:
            print("Thank you....!")
            exit()
        else:
            print("Invalid input")

main()
