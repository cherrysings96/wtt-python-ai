import functools

class StudyTracker2:
    def __init__(self, name="", topic="", isTheoryDone=False, isPracticalDone=False):
        self.name = name
        self.topic = topic
        self.isTheoryDone = isTheoryDone
        self.isPracticalDone = isPracticalDone

    def get_details(self):
        print("\n------------ Study Tracker Input ------------")
        self.name = input("Enter your name: ")
        self.topic = input("Enter the topic: ")
        # .strip().lower() removes extra spaces and makes it lowercase
        self.isTheoryDone = input(f"Is theory for {self.topic} done? ").strip().lower()
        self.isPracticalDone = input(f"Is practical for {self.topic} done? ").strip().lower()
    
    def show_dashboard(self):
        print("\n------------ Study Tracker Output ------------")
        print(f"Name:  {self.name}")
        print(f"Topic: {self.topic}")

        # Check for "yes" (covers all cases because of .lower() earlier)
        theory_points = 50 if self.isTheoryDone == "yes" else 0
        pract_points = 50 if self.isPracticalDone == "yes" else 0

        # Visual symbols
        print(f"Theory:    {'✅' if theory_points == 50 else '❌'}")
        print(f"Practical: {'✅' if pract_points == 50 else '❌'}")

        finalPercent = theory_points + pract_points
        print(f"Percentage: {finalPercent}%")

        if finalPercent == 50:
            print("Good job! You're halfway there!")
        elif finalPercent == 100:
            print("Very good! You completed the topic.")
        else:
            print("Keep working. You can do it!!")

# --- RUN ---
s = StudyTracker2()
s.get_details()
s.show_dashboard()