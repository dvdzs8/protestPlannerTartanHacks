import tkinter as tk
from tkinter import ttk


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('Protest Organizor Toolkit')
        self.mainframe = tk.Frame(self.root, background='#ffffdd')
        self.mainframe.pack(fill='both', expand=True)

        return


if __name__ == '__main__':
    App()