import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Quiz Game")
        self.score = 0
        self.current_question = None
        self.current_question_index = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],
                "correct_answer": "C"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
                "correct_answer": "B"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Dolphin"],
                "correct_answer": "B"
            },
            {
                "question": "Which gas do plants absorb from the atmosphere?",
                "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
                "correct_answer": "C"
            }
        ]

        self.root.configure(bg="lightblue") 
        self.quiz_frame = tk.Frame(root, bg="black")
        self.quiz_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 14), fg="white", bg="black")
        self.question_label.pack(pady=(0, 10), fill="both", expand=True)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.quiz_frame, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(self.option_buttons[i]))
            self.option_buttons.append(button)
            button.pack(fill="x", padx=20, pady=5, ipady=5)  
            button.configure(bg=random.choice(["lightblue", "lightgreen", "lightpink", "lightyellow"]))  

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            self.question_label.config(text=f"Q{self.current_question_index + 1}: {self.current_question['question']}")
            for i in range(4):
                if "options" in self.current_question:
                    self.option_buttons[i].config(text=self.current_question["options"][i])
                else:
                    self.option_buttons[i].config(text=f"Fill in the blank")
        else:
            self.show_score()

    def check_answer(self, button):
        user_answer = button.cget("text")[0]  
        correct_answer = self.current_question["correct_answer"][0]
        if user_answer == correct_answer:
            self.score += 1
        else:
            messagebox.showinfo("Incorrect", f"The correct answer is {self.current_question['correct_answer']}")

        self.current_question_index += 1
        self.next_question()

    def show_score(self):
        score_window = tk.Toplevel(self.root)
        score_window.title("Quiz Score")
        score_label = tk.Label(score_window, text=f"Your Score: {self.score}/{len(self.option_buttons)}", font=("Arial", 18))
        score_label.pack(pady=20)
        score_window.mainloop()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry("600x400")  
    root.mainloop()

if __name__ == "__main__":
    main()
