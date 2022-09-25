from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas = Canvas(height=250, width=300, background='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, borderwidth=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img, borderwidth=0)
        self.false_button.grid(row=2, column=1, pady=20)


        self.window.mainloop()