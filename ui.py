from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #window
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20, bg=THEME_COLOR)

        #labels
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg= "white")
        self.score_label.grid(row=0, column=1)

        #canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some question text",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #buttons
        false_image = PhotoImage(file="./images/false.png")
        true_image = PhotoImage(file="./images/true.png")
        self.false_button = Button(self.window, image= false_image, highlightthickness=0, command= self.check_false)
        self.false_button.grid(row=2,column=1)
        self.true_button = Button(self.window, image= true_image, highlightthickness=0, command= self.check_true)
        self.true_button.grid(row=2,column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """grabs next question and resets canvas"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # at the end of quiz, turn off buttons and tell user.
            self.canvas.itemconfig(self.question_text, text= "You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, func= self.get_next_question)























