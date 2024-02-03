import tkinter as tk
from tkinter import ttk


class Back():

    col1 = "#ffffdd" #background
col2 = "#ffffff"

    def __init__(self):

        #just the main empty background
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('Protest Organizor Toolkit')
        self.mainframe = tk.Frame(self.root, background=col1)
        self.mainframe.pack(fill='both', expand=True)
        
        #banner
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10)


        self.root.mainloop()
        return


if __name__ == '__main__':
    Back()