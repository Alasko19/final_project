import tkinter as tk
from questions import Questions

root = tk.Tk()
root.title("Quiz exam system")
root.geometry("500x350")

student_name = tk.StringVar()
selected_answer = tk.StringVar()
current_question = 0
score = 0

def start_quiz():
    title_Label.pack_forget()
    name_Label.pack_forget()
    name_entry.pack_forget()
    start_button.pack_forget()
    
    show_question()

def show_question():
    question_data = Questions[current_question]
    question_Label.config(text=question_data["Questions"])
    options = question_data["options"]

    selected_answer.set("")

    option1.config(text=options[0], value=options[0])
    option2.config(text=options[1], value=options[1])
    option3.config(text=options[2], value=options[2])
    option4.config(text=options[3], value=options[3])

    question_Label.pack(pady=20)
    option1.pack(anchor="w", padx=40)
    option2.pack(anchor="w", padx=40)
    option3.pack(anchor="w", padx=40)
    option4.pack(anchor="w", padx=40)
    next_button.pack(pady=20)

def next_question():
    global current_question
    global score

    answer = selected_answer.get()

    if answer == Questions[current_question]["Answer"]:
        score += 1

    current_question += 1
    if current_question < len(Questions):
        show_question()
    else:
        show_result()

def show_result():
    question_Label.config(
        text=f"{student_name.get()}, you scored {score} out of {len(Questions)}"
    )

    with open("scores.txt", "a") as file:
        file.write(f"{student_name.get()} - {score}/{len(Questions)}\n")

    option1.pack_forget()
    option2.pack_forget()
    option3.pack_forget()
    option4.pack_forget()
    next_button.pack_forget()


title_Label = tk.Label(root, text="Python Quiz System", font=("Arial", 18))
title_Label.pack(pady=20)

name_Label = tk.Label(root, text="Enter your name: ")
name_Label.pack()

name_entry = tk.Entry(root, textvariable=student_name, width=30)
name_entry.pack(pady=30)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack(pady=20)

question_Label = tk.Label(root, text="", wraplength=400)

option1 = tk.Radiobutton(root, variable=selected_answer)
option2 = tk.Radiobutton(root, variable=selected_answer)
option3 = tk.Radiobutton(root, variable=selected_answer)
option4 = tk.Radiobutton(root, variable=selected_answer)

next_button = tk.Button(
    root, text="Next", command=next_question
)



root.mainloop()