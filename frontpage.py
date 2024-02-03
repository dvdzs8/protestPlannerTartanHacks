import tkinter as tk
from tkinter import ttk

col1 = "#ffffdd" #background
col2 = "#ffffff"

class Back():

    def __init__(self):
        #just the main empty background
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('Protest Organizor Toolkit')
        self.mainframe = tk.Frame(self.root, background=col2)
        self.mainframe.pack(fill='both', expand=True)
        
        def create_header():
            banner = ttk.Entry(self.root, font = ('Oxygen', 16), wrap=tk.WORD, width=1920, height=10)
            banner.pack(row=1, column=0, pady=10)
            #banner.pack(pady=10)
            banner.insert(tk.END,'HI')
        
        #banner
            
        self.banner = create_header()
        #self.banner = tk.Text(font = ('Oxygen', 16), bg="blue", pady= 0, borderwidth=2, relief="solid", width=1920, height=100)
        #self.banner.pack

        

        




        #david's bottom 2 squares

        contactBox = tk.Text()

        self.root.mainloop()
        return


if __name__ == '__main__':
    Back()