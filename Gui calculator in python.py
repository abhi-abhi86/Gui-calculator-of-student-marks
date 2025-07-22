import tkinter as tk
from tkinter import messagebox


def calculate_result():
    try:
        name = name_entry.get().upper()
        sub1 = int(sub1_entry.get())
        sub2 = int(sub2_entry.get())
        sub3 = int(sub3_entry.get())
        sub4 = int(sub4_entry.get())
        sub5 = int(sub5_entry.get())

        if not all(0 <= mark <= 100 for mark in [sub1, sub2, sub3, sub4, sub5]):
            messagebox.showwarning("Invalid Marks", "Please enter marks between 0 and 100.")
            return

        total_marks = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (total_marks / 500) * 100

        if percentage == 100:
            grade = "A+"
            comment = "VERY GOOD 👌"
        elif 90 < percentage < 100:
            grade = "A"
            comment = "GOOD 😃"
        elif 75 < percentage <= 90:
            grade = "B"
            comment = "AVERAGE 😐"
        elif 50 < percentage <= 75:
            grade = "C"
            comment = "PASS"
        elif 25 < percentage <= 50:
            grade = "D"
            comment = "PASS - C GRADE"
        else:
            grade = "F"
            comment = "FAIL ❌"

        result_text.set(f"\n📋 Report Card for {name}\n"
                        f"Total Marks: {total_marks}/500\n"
                        f"Percentage: {percentage:.2f}%\n"
                        f"Grade: {grade}\n"
                        f"Comment: {comment}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer marks.")



root = tk.Tk()
root.title("Student Marks to Percentage Calculator")
root.geometry("450x500")
root.config(bg="#f0f0f0")


tk.Label(root, text="Student Name:", bg="#f0f0f0").pack()
name_entry = tk.Entry(root)
name_entry.pack()

sub_entries = []
labels = ["Subject 1:", "Subject 2:", "Subject 3:", "Subject 4:", "Subject 5:"]
for label in labels:
    tk.Label(root, text=label, bg="#f0f0f0").pack()

sub1_entry = tk.Entry(root)
sub2_entry = tk.Entry(root)
sub3_entry = tk.Entry(root)
sub4_entry = tk.Entry(root)
sub5_entry = tk.Entry(root)

sub1_entry.pack()
sub2_entry.pack()
sub3_entry.pack()
sub4_entry.pack()
sub5_entry.pack()


tk.Button(root, text="Calculate Result", command=calculate_result, bg="#4CAF50", fg="white").pack(pady=10)


result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, bg="#f0f0f0", justify="left").pack()


root.mainloop()
