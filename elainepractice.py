import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x200')
        self.root.title('Text App')
        self.mainframe = tk.Frame(self.root, background='yellow')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe,text='Welcome to your protestor toolkit', background='white', font=("Times New Roman", 30))
        self.text.grid(row=0, column=0)
        self.root.mainloop()
        return
    

if __name__ == '__main__':
    App()