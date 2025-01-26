import tkinter as tk
from tkinter import messagebox

def convert_base():
    number = number_entry.get()
    base = int(base_entry.get())
    base2 = int(base2_entry.get())
    try:
        numberin10 = int(number, base)
        result = ''
        if base2 == 16 or 15 or 14 or 13 or 12 or 11:  ##jesli chcesz wynik bez liczb, wypierdol na 16 TYLKO!!!
            while numberin10 > 0:
                if numberin10 % base2 == 10:
                    result = "A" + result
                elif numberin10 % base2 == 11:
                    result = "B" + result
                elif numberin10 % base2 == 12:
                    result = "C" + result
                elif numberin10 % base2 == 13:
                    result = "D" + result
                elif numberin10 % base2 == 14:
                    result = "E" + result
                elif numberin10 % base2 == 15:
                    result = "F" + result
                else:
                    result = str(numberin10 % base2) + result
                numberin10 //= base2
        while numberin10 > 0:
            result = str(numberin10 % base2) + result
            numberin10 //= base2
        result_label.config(text="Result: " + result)
        messagebox.Message("Result: " + result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.configure(bg='black', padx=25, pady=25)

tk.Label(root, text="Enter number:", bg='black', fg='white').pack()
number_entry = tk.Entry(root)
number_entry.pack()

tk.Label(root, text="Enter base:", bg='black', fg='white').pack()
base_entry = tk.Entry(root)
base_entry.pack()

tk.Label(root, text="Enter base to convert to:", bg='black', fg='white').pack()
base2_entry = tk.Entry(root)
base2_entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert_base)
convert_button.pack()

result_label = tk.Label(root, text="Result: ", bg='black', fg='white')
result_label.pack()

root.mainloop()
