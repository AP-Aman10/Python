from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Student:
    def __init__(self, name):
        self.name = name.title()
        self.subjects = {
            "Hindi": 0,
            "English": 0,
            "Maths": 0,
            "Science": 0,
            "Social Science": 0,
            "Computer": 0
        }

    def input_marks(self):
        print(f"\n📝 {Fore.CYAN}Enter marks for {self.name}:{Style.RESET_ALL}")
        print(Fore.LIGHTBLACK_EX + "-" * 45)
        for subject in self.subjects:
            while True:
                try:
                    mark = float(input(f"  {subject:<15}: "))
                    if 0 <= mark <= 100:
                        self.subjects[subject] = mark
                        break
                    else:
                        print(Fore.RED + "⚠️  Please enter marks between 0 and 100.")
                except ValueError:
                    print(Fore.RED + "🚫 Invalid input! Please enter a number.")
        print(Fore.LIGHTBLACK_EX + "-" * 45)

    def remark_for_mark(self, mark):
        """Return a performance remark based on mark range."""
        if mark >= 90:
            return "Excellent 🏆"
        elif mark >= 80:
            return "Very Good 👏"
        elif mark >= 70:
            return "Good 👍"
        elif mark >= 60:
            return "Average 📘"
        elif mark >= 40:
            return "Needs Improvement 📝"
        else:
            return "Fail 😔"

    def color_for_mark(self, mark):
        """Return a color based on mark range."""
        if mark >= 90:
            return Fore.GREEN + Style.BRIGHT
        elif mark >= 80:
            return Fore.LIGHTGREEN_EX + Style.BRIGHT
        elif mark >= 70:
            return Fore.YELLOW + Style.BRIGHT
        elif mark >= 60:
            return Fore.LIGHTYELLOW_EX + Style.BRIGHT
        elif mark >= 40:
            return Fore.CYAN + Style.BRIGHT
        else:
            return Fore.RED + Style.BRIGHT

    def calculate_total(self):
        return sum(self.subjects.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.subjects)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return Fore.GREEN + "A+ (Excellent 🏆)" + Style.RESET_ALL
        elif avg >= 80:
            return Fore.LIGHTGREEN_EX + "A (Very Good 👏)" + Style.RESET_ALL
        elif avg >= 70:
            return Fore.YELLOW + "B (Good 👍)" + Style.RESET_ALL
        elif avg >= 60:
            return Fore.LIGHTYELLOW_EX + "C (Average 📘)" + Style.RESET_ALL
        elif avg >= 50:
            return Fore.CYAN + "D (Needs Improvement 📝)" + Style.RESET_ALL
        else:
            return Fore.RED + "F (Fail 😔)" + Style.RESET_ALL

    def show_result(self):
        line = Fore.MAGENTA + "=" * 70 + Style.RESET_ALL
        print("\n" + line)
        print(Fore.LIGHTBLUE_EX + f"📘 FINAL REPORT CARD for {self.name.upper()}".center(70))
        print(line)

        # Subject details
        print(Fore.LIGHTBLACK_EX + f"{'Subject':<20} {'Marks':<10} {'Remarks':<25}")
        print(Fore.LIGHTBLACK_EX + "-" * 70)
        for subject, mark in self.subjects.items():
            color = self.color_for_mark(mark)
            remark = self.remark_for_mark(mark)
            print(f"{subject:<20} {color}{mark:<10.1f}{Style.RESET_ALL} {remark}")

        total = self.calculate_total()
        avg = self.calculate_average()
        grade = self.calculate_grade()

        print(Fore.LIGHTBLACK_EX + "-" * 70)
        print(f"{Fore.CYAN}🧮 Total Marks: {Fore.WHITE}{total:.2f}")
        print(f"{Fore.CYAN}📊 Average Marks: {Fore.WHITE}{avg:.2f}")
        print(f"{Fore.CYAN}🎓 Grade: {grade}")
        print(line)

        # Remark based on overall performance
        if avg >= 90:
            final_remark = Fore.GREEN + "🌈 Outstanding performance! Keep shining bright! 💪"
        elif avg >= 80:
            final_remark = Fore.LIGHTGREEN_EX + "💫 Excellent work! Keep up the great effort!"
        elif avg >= 70:
            final_remark = Fore.YELLOW + "😊 Good job! Push a little harder for excellence!"
        elif avg >= 60:
            final_remark = Fore.LIGHTYELLOW_EX + "📘 Fair effort. Consistency will lead to success!"
        elif avg >= 40:
            final_remark = Fore.CYAN + "📝 Needs improvement. You can do it with focus!"
        else:
            final_remark = Fore.RED + "😔 Don’t give up! Work harder and come back stronger!"

        print(final_remark)
        print(line)


# --- Main Program ---
if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + "\n✨ Welcome to the Student Report Card Generator ✨")
    print(Fore.LIGHTBLACK_EX + "-" * 70)
    name = input(Fore.LIGHTBLUE_EX + "Enter Student Name: " + Style.RESET_ALL)
    student = Student(name)
    student.input_marks()
    student.show_result()
    print(Fore.LIGHTMAGENTA_EX + "\n✅ Report generated successfully! 🎉\n")
