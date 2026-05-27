# Smart Quiz + Leaderboard System 
#  Idea:
# A Python-based quiz app where students answer questions and get ranked.
#  Features:
# Store multiple-choice questions
# Show one question at a time
# Calculate score automatically
# Show final result (Pass / Fail)
# Maintain leaderboard (top scores)
# Store student names and scores
# Concepts Used (Python only):
# Loops
# Conditions
# Functions
# Lists / Dictionaries
# File handling

# ---------------- QUESTIONS ---------------- #

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kerala"],
        "answer": "B"
    },

    {
        "question": "Which language is used for Python?",
        "options": ["A. HTML", "B. Java", "C. Python", "D. CSS"],
        "answer": "C"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Control Processing Unit"
        ],
        "answer": "B"
    },

    {
        "question": "Which keyword is used for loops in Python?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "answer": "C"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]

# ---------------- START QUIZ ---------------- #

def start_quiz():

    print("\n===== SMART QUIZ SYSTEM =====")

    student_name = input("Enter your name: ")

    score = 0

    # Loop through questions
    for q in questions:

        print("\n" + q["question"])

        # Display options
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        # Check answer
        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct answer is:", q["answer"])

    # Final Result
    print("\n===== RESULT =====")
    print("Student:", student_name)
    print("Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    # Pass / Fail
    if percentage >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # Save score
    save_score(student_name, score)

    # Show leaderboard
    show_leaderboard()


# ---------------- SAVE SCORE ---------------- #

def save_score(name, score):

    file = open("leaderboard.txt", "a")

    file.write(name + "," + str(score) + "\n")

    file.close()


# ---------------- LEADERBOARD ---------------- #

def show_leaderboard():

    print("\n===== LEADERBOARD =====")

    try:

        file = open("leaderboard.txt", "r")

        data = file.readlines()

        leaderboard = []

        for line in data:

            name, score = line.strip().split(",")

            leaderboard.append((name, int(score)))

        # Sort by score descending
        leaderboard.sort(key=lambda x: x[1], reverse=True)

        # Display top 5 scores
        rank = 1

        for entry in leaderboard[:5]:
            print(rank, ".", entry[0], "-", entry[1])
            rank += 1

        file.close()

    except FileNotFoundError:
        print("No leaderboard data found.")


# ---------------- MAIN PROGRAM ---------------- #

while True:

    start_quiz()

    again = input("\nDoes another student want to take the quiz? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using Smart Quiz System!")
        break