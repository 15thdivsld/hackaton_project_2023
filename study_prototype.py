import time
import random

motivational_quotes = [
    "A person who never made a mistake never tried anything new - Albert Einstein",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The man who does not read books has no advantage over the one who cannot read them. - Mark Twain",
    "Procrastination makes easy things hard and hard things harder. - Mason Cooley",
]

class Student:
    def __init__(self, name, daily_goal):
        self.name = name
        self.daily_goal = daily_goal
        self.total_study_time = 0
        self.points = 0
        self.badges = []

    def earn_points(self, study_duration):
        self.points += study_duration // 5 

    def check_goal_completion(self):
        if self.total_study_time >= self.daily_goal:
            self.earn_badge("Daily Goal Achiever")

    def earn_badge(self, badge_name):
        self.badges.append(badge_name)
        print(f"Congratulations, {self.name}! You earned the '{badge_name}' badge.")

def main():
    print("Welcome to the Study Motivation Program")
    student_name = input("Enter your name: ")
    daily_study_goal = int(input("Set your daily study goal (in minutes): "))

    student = Student(student_name, daily_study_goal)
    
    while student.total_study_time < student.daily_goal:
        input("Press Enter when you start studying...")
        study_start_time = time.time()
        
        input("Press Enter when you finish studying...")
        study_end_time = time.time()
        
        study_duration = round((study_end_time - study_start_time) / 60, 2) 
        student.total_study_time += study_duration
        student.earn_points(study_duration)
        
        print(f"Great job, {student.name}! You studied for {study_duration} minutes.")
        print(random.choice(motivational_quotes))  
        print(f"Total Points: {student.points}")

        if student.total_study_time >= student.daily_goal:
            student.check_goal_completion()
            print("Congratulations! You've reached your daily goal.")
        else:
            remaining_time = student.daily_goal - student.total_study_time
            print(f" You have {remaining_time} minutes left to reach your goal.")

    print("Well done for today, keep up the good work!")
    print(f"Total Points Earned: {student.points}")
    if student.badges:
        print(f"Badges Earned: {', '.join(student.badges)}")

if __name__ == "__main__":
    main()