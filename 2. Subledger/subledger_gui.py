import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import time

def run_script():
    for i in range(101):
        time.sleep(0.05)
        progress_var.set(i)
        window.update_idletasks()

def start_progress():
    global progress_bar, progress_var, label2, button1, label3, button2, button3
    label1.pack_forget()
    button1.pack_forget()
    label2 = tk.Label(window, text="Running script...")
    label2.pack()
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(window, variable=progress_var, maximum=100)
    progress_bar.pack()
    window.update_idletasks()
    run_script()
    progress_bar.pack_forget()
    label2.pack_forget()
    label3 = tk.Label(window, text="Do you want to run the script again?")
    button2 = tk.Button(window, text="Yes", command=restart_program)
    button3 = tk.Button(window, text="No", command=stop_program)
    label3.pack(side=tk.LEFT)
    button2.pack(side=tk.LEFT)
    button3.pack(side=tk.LEFT)

def restart_program():
    label3.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    label1.pack()
    button1.pack()

def stop_program():
    window.destroy()

def start_program():
    global label1, button1, window
    window = tk.Tk()
    window.title("My App")
    window.geometry("600x400")
    label1 = tk.Label(window, text="Welcome to my app!")
    label1.pack()
    button1 = tk.Button(window, text="Run script", command=start_progress)
    button1.pack()
    window.mainloop()

start_program()