import tkinter as tk
from tkinter import ttk

col1 = "#c8c8a9" #background of squares
col2 = "#ffcdad"  #background 
col3 = '#fe4365' #header

class Back():

    def __init__(self):
        #just the main empty background
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('Protest Organizor Toolkit')
        self.mainframe = tk.Frame(self.root, background=col2)
        self.mainframe.pack(fill='both', expand=True)
        
        def create_header():
            banner = tk.Text(self.mainframe, padx=10, pady=10, font = ("Oxygen", 16), bg=col3, relief="solid", borderwidth=2, wrap=tk.WORD, width=100, height=1)
            #banner.grid(row=1, column=0, sticky='NWES') #padding of 10 pixels. both above and below
            # banner = ttk.Entry(self.root, font = ('Oxygen', 16), wrap=tk.WORD, width=1920, height=10)
            # banner.pack(row=1, column=0, pady=10)
            banner.pack()
            banner.insert(tk.END, "Title and organizers: ")
            # banner.insert(tk.END,'HI')
        
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