import tkinter as tk
from tkinter import messagebox,ttk

def mood():
    mood = your_mood.get()
    if mood == "Happy":
        messagebox.showinfo("Your Message","That's wonderful!, Keep smiling and be vibrant and positive.")
    elif mood == "Sad":
        messagebox.showinfo("Your Message","Take a deep breath, and think every day is great and you are doing great.")
    elif mood == "Angry":
        messagebox.showinfo("Your Message","Keep calm , everyone is human and human nature should not be judged.")
    elif mood == "Anxious":
        messagebox.showinfo("Your Message","You are best in your own, just go and show the world your might,")
    else:
        messagebox.showinfo("Your Message","Please select a mood from the dropdown menu.")

root = tk.Tk()
root.title("Mood based Message Bot")
root.geometry("400x200")

your_mood = tk.StringVar()
mood_options = ["Happy", "Sad", "Angry", "Anxious"]
your_mood.set("Select your mood")
mood_menu = ttk.Combobox(root, textvariable=your_mood, values=mood_options)
mood_menu.pack(pady=20)
# mood_menu.bind("<<ComboboxSelected>>", lambda event: mood())
mood_button = tk.Button(root, text="Get Message", command=mood)
mood_button.pack(pady=10)
root.resizable(False, False)
root.mainloop()

