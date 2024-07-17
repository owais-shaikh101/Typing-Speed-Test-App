from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
import random

word_list = [
    "abandon", "ability", "absence", "academy", "accept", "account", "achieve",
    "activity", "affect", "agency", "amount", "analysis", "answer", "article",
    "attitude", "balance", "benefit", "beyond", "brought", "capital", "capture",
    "change", "compare", "concept", "create", "culture", "decade", "decide",
    "deliver", "demand", "design", "detail", "device", "discover", "display",
    "effect", "enough", "evidence", "feature", "federal", "further", "general",
    "healthy", "history", "impact", "include", "increase", "income",
    "inform", "interest", "journal", "journey", "language", "library", "manage",
    "market", "method", "modern", "moment", "natural", "notable", "object",
    "option", "partner", "pattern", "perform", "present", "produce", "project",
    "purpose", "quality", "record", "reflect", "region", "reliability", "response",
    "secure", "section", "service", "significant", "society", "solution", "status",
    "support", "system", "teacher", "theory", "thought", "transfer", "unique",
    "update", "utility", "variety", "volume", "witness", "wonder", "without",
    "yesterday", "yourself", "contact"
]

current_word = random.choice(word_list)
seconds = 60
total_keys_pressed = 0

def start():
    global seconds
    if seconds > 0:
        if seconds == 60:
            time_label.config(text="1:00")
        elif 60 > seconds >= 10:
            time_label.config(text=f"0:{str(seconds)}")
        else:
            time_label.config(text=f"0:0{str(seconds)}")
        seconds -= 1
        root.after(1000, start)



def key_press(event):
    global total_keys_pressed
    total_keys_pressed += 1

def change_word(event):
    word_input.delete(0, 'end')
    next_word = random.choice(word_list)
    word_label.config(text=next_word)

def show_results():
    heading_label.destroy()
    word_label.destroy()
    word_input.destroy()
    time_label.destroy()
    wpm = int(total_keys_pressed / 5)
    wpm_label.config(text=f"Words per Minute = {str(wpm)}")
    wpm_label.pack()
    restart_button.pack()

def restart():
    global seconds
    global total_keys_pressed
    global heading_label
    global word_label
    global word_input
    global time_label
    global wpm_label
    global restart_button

    wpm_label.destroy()
    restart_button.destroy()

    seconds = 60
    total_keys_pressed = 0
    heading_label = Label(root, text="Start Typing", bg="#000000", fg="#00FFFF", font=("Arial", 24, "bold"), pady=20)
    heading_label.pack()
    word_label = Label(root, text=current_word, bg="#000000", fg="#FFFFFF", font=("Arial", 20), pady=20)
    word_label.pack()
    word_input = Entry(root, bg="#555555", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Arial", 18))
    word_input.pack()
    word_input.focus()
    time_label = Label(root, text="1:00", bg="#000000", fg="#FFFF00", pady=10, font=("Arial", 16))
    time_label.pack()
    wpm_label = Label(root, text="", pady=50, bg="#000000", fg="#00FF00", font=("Comic Sans MS", 30, "bold"))
    restart_button = Button(root, text="Restart", bg="#005500", fg="#FFFFFF", activebackground="#000000",
                            activeforeground="#FFFFFF", padx=10, pady=5, font=("Arial", 26, "bold"), cursor="hand2",
                            command=restart)
    start()
    root.after(60500, show_results)

root = Tk()
root.title("Typing Speed Test App")
root.geometry("600x400")
root.config(bg="#000000")
heading_label = Label(root, text="Start Typing", bg="#000000", fg="#00FFFF", font=("Arial", 24, "bold"), pady=20)
heading_label.pack()
word_label = Label(root, text=current_word, bg="#000000", fg="#FFFFFF", font=("Arial", 20), pady=20)
word_label.pack()
word_input = Entry(root, bg="#555555", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Arial", 18))
word_input.pack()
word_input.focus()
time_label = Label(root, text="1:00", bg="#000000", fg="#FFFF00", pady=10, font=("Arial", 16))
time_label.pack()
wpm_label = Label(root, text="", pady=50, bg="#000000", fg="#00FF00", font=("Comic Sans MS", 30, "bold"))
restart_button = Button(root, text="Restart", bg="#005500", fg="#FFFFFF", activebackground="#000000", activeforeground="#FFFFFF", padx=10, pady=5, font=("Arial", 26, "bold"), cursor="hand2", command=restart)
start()
root.bind("<Key>", key_press)
root.bind("<space>", change_word)
root.after(60500, show_results)
root.mainloop()