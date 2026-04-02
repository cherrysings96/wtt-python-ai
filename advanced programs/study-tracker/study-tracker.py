import functools

# 1. THE TOPIC CLASS (Upgraded for 3 pillars + progress)
class StudyTopic:
    def __init__(self, name, theory=False, practical=False, logical=False):
        self.name = name
        self.theory = theory
        self.practical = practical
        self.logical = logical

    # NEW: Individual topic progress
    def progress(self):
        completed = sum([self.theory, self.practical, self.logical])
        return (completed / 3) * 100

    # UPDATED: Status with progress + label
    def status(self):
        t_stat = "✅" if self.theory else "❌"
        p_stat = "✅" if self.practical else "❌"
        l_stat = "✅" if self.logical else "❌"
        prog = self.progress()

        # Smart label
        if prog == 100:
            level = "🏆 Mastered"
        elif prog >= 66:
            level = "🔥 Strong"
        elif prog > 0:
            level = "⚠️ Improving"
        else:
            level = "❌ Not Started"

        return f"{self.name:15} | Theory:{t_stat} Programs:{p_stat} Logical:{l_stat} | 📊 {prog:.1f}% | {level}"


# 2. THE TRACKER SYSTEM
class ProgressTracker:
    def __init__(self):
        self.collection = []

    def add_from_input(self):
        name = input("\n📚 Enter Topic Name: ").strip()
        t_input = input("   Theory Done? (y/n): ").lower() == 'y'
        p_input = input("   Practical Done? (y/n): ").lower() == 'y'
        l_input = input("   Logical Mastery Done? (y/n): ").lower() == 'y'
        
        new_topic = StudyTopic(name, t_input, p_input, l_input)
        self.collection.append(new_topic)
        print(f"✨ '{name}' added successfully!")

    def show_dashboard(self):
        if not self.collection:
            print("\nNothing to show. Add some topics first!")
            return

        print("\n" + "="*80)
        print(f"{'TOPIC':15} | {'DETAILED PROGRESS'}")
        print("-" * 80)
        
        for topic in self.collection:
            print(topic.status())

        # --- OVERALL ANALYSIS ---
        total_topics = len(self.collection)
        t_done = len([t for t in self.collection if t.theory])
        p_done = len([t for t in self.collection if t.practical])
        l_done = len([t for t in self.collection if t.logical])
        
        # Fully mastered topics
        fully_mastered = list(filter(lambda x: x.theory and x.practical and x.logical, self.collection))
        
        # Overall progress
        total_possible_checks = total_topics * 3
        actual_checks = t_done + p_done + l_done
        progress_perc = (actual_checks / total_possible_checks) * 100

        print("-" * 80)
        print(f"📖 Theory: {t_done}/{total_topics}  🛠️ Practical: {p_done}/{total_topics}  🧠 Logical: {l_done}/{total_topics}")
        print(f"🏆 Fully Mastered: {len(fully_mastered)}/{total_topics} Topics")
        print(f"📊 Overall Progress: {progress_perc:.1f}%")
        print("-" * 80)

        # Smart Feedback
        stats = {"Theory": t_done, "Practical": p_done, "Logical": l_done}
        weakest = min(stats, key=stats.get)

        if progress_perc == 100:
            print("🌟 BRILLIANT! You have reached 100% mastery!")
        elif progress_perc >= 70:
            print(f"🔥 Great momentum! Polish your {weakest} skills to reach the finish line.")
        elif progress_perc > 0:
            print(f"💡 Tip: Your {weakest} pillar is trailing behind. Focus there next!")

        print("="*80)


# --- INTERACTIVE MENU ---
def main():
    tracker = ProgressTracker()
    print("🚀 Study Progress Analyzer Loaded!")
    
    while True:
        print("\n1. Add Topic  2. View Dashboard  3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            tracker.add_from_input()
        elif choice == "2":
            tracker.show_dashboard()
        elif choice == "3":
            print("Keep up the study grind! Goodbye.")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()