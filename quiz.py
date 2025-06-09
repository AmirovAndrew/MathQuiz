import tkinter as tk
from tkinter import font, ttk
import random

class MathQuizApp:
    def __init__(self, root):
        """Initializes the quiz application GUI and its components."""
        self.root = root
        self.root.title("Math Quiz for Kids!")
        
        # --- Color Scheme ---
        self.BG_COLOR = "#E0F7FA"
        self.BUTTON_COLOR = "#4CAF50"
        self.BUTTON_ACTIVE_COLOR = "#81C784"
        self.CORRECT_COLOR = "#388E3C"
        self.INCORRECT_COLOR = "#D32F2F"

        self.root.config(bg=self.BG_COLOR)
        self.root.geometry("400x500")

        # --- Instance Variables ---
        self.score = 0
        self.correct_answer = 0
        self.question_count = 0
        self.score_history = []

        # --- Fonts and Media ---
        self.default_font = font.Font(family="Comic Sans MS", size=16)
        self.question_font = font.Font(family="Comic Sans MS", size=26, weight="bold")
        self.feedback_font = font.Font(family="Comic Sans MS", size=18)
        self.load_media() # Now only loads images

        # --- GUI Widgets ---
        self.score_label = tk.Label(root, text="Score: 0", font=self.default_font, bg=self.BG_COLOR)
        self.score_label.pack(pady=10)
        self.question_label = tk.Label(root, text="", font=self.question_font, bg=self.BG_COLOR)
        self.question_label.pack(pady=20)
        self.answer_entry = tk.Entry(root, font=self.default_font, width=10, justify='center', bd=2, relief="solid")
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        button_frame = tk.Frame(root, bg=self.BG_COLOR)
        button_frame.pack(pady=10)
        
        self.submit_button = tk.Button(button_frame, text="Submit", font=self.default_font, command=self.check_answer,
                                       bg=self.BUTTON_COLOR, fg="white", activebackground=self.BUTTON_ACTIVE_COLOR,
                                       activeforeground="white", bd=0, padx=20, pady=5)
        self.submit_button.pack(side="left", padx=10)
        
        self.scoreboard_button = tk.Button(button_frame, text="History", font=self.default_font, command=self.show_scoreboard,
                                           bg="#FFA726", fg="white", bd=0, padx=20, pady=5)
        self.scoreboard_button.pack(side="left", padx=10)
        
        self.feedback_text_label = tk.Label(root, text="", font=self.feedback_font, bg=self.BG_COLOR)
        self.feedback_text_label.pack(pady=5)
        self.feedback_icon_label = tk.Label(root, bg=self.BG_COLOR)
        self.feedback_icon_label.pack(pady=10)
        
        self.next_question()

    def load_media(self):
        """Loads all external image files."""
        # --- Load Images ---
        try:
            self.correct_image = tk.PhotoImage(file="correct.png")
            self.incorrect_image = tk.PhotoImage(file="incorrect.png")
        except tk.TclError:
            print("Info: Could not find image files 'correct.png' or 'incorrect.png'. Image feedback disabled.")
            self.correct_image, self.incorrect_image = None, None

    def generate_addition_task(self):
        num1, num2 = random.randint(1, 99), random.randint(1, 99)
        return f"{num1} + {num2}", num1 + num2

    def generate_subtraction_task(self):
        num1, num2 = random.randint(1, 99), random.randint(1, 99)
        if num1 < num2: num1, num2 = num2, num1
        return f"{num1} - {num2}", num1 - num2

    def generate_multiplication_task(self):
        while True:
            num1, num2 = random.randint(1, 20), random.randint(1, 20)
            if num1 * num2 < 150: return f"{num1} * {num2}", num1 * num2
    
    def generate_division_task(self):
        answer = random.randint(2, 12); divisor = random.randint(2, 12)
        return f"{answer * divisor} / {divisor}", answer

    def next_question(self):
        self.question_count += 1
        self.submit_button.config(state="normal")
        self.answer_entry.config(state="normal")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus_set()
        self.feedback_text_label.config(text="")
        self.feedback_icon_label.config(image='')
        
        task_functions = [self.generate_addition_task, self.generate_subtraction_task, self.generate_multiplication_task, self.generate_division_task]
        self.current_question_text, self.correct_answer = random.choice(task_functions)()
        self.question_label.config(text=self.current_question_text)

    def check_answer(self, event=None):
        user_answer_str = self.answer_entry.get()
        result_text = ""
        try:
            user_answer = int(user_answer_str)
            if user_answer == self.correct_answer:
                self.score += 1
                self.feedback_text_label.config(text="Great Job!", fg=self.CORRECT_COLOR)
                if self.correct_image: self.feedback_icon_label.config(image=self.correct_image)
                result_text = "Correct"
            else:
                self.score = 0
                feedback_text = f"The answer was {self.correct_answer}"
                self.feedback_text_label.config(text=feedback_text, fg=self.INCORRECT_COLOR)
                if self.incorrect_image: self.feedback_icon_label.config(image=self.incorrect_image)
                result_text = "Incorrect"
        except ValueError:
            self.feedback_text_label.config(text="Numbers only, please!", fg="orange")
            result_text = "Invalid"
        
        self.score_history.append({
            "num": self.question_count,
            "question": self.current_question_text,
            "answer": user_answer_str,
            "result": result_text
        })
        
        self.score_label.config(text=f"Score: {self.score}")
        self.submit_button.config(state="disabled")
        self.answer_entry.config(state="disabled")
        self.root.after(2000, self.next_question)

    def show_scoreboard(self):
        scoreboard_window = tk.Toplevel(self.root)
        scoreboard_window.title("History")
        scoreboard_window.geometry("500x300")
        scoreboard_window.config(bg=self.BG_COLOR)
        columns = ('question', 'answer', 'result')
        tree = ttk.Treeview(scoreboard_window, columns=columns, show='headings')
        tree.heading('question', text='Question')
        tree.heading('answer', text='Your Answer')
        tree.heading('result', text='Result')
        for record in self.score_history:
            tree.insert('', tk.END, values=(record['question'], record['answer'], record['result']))
        tree.pack(expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
