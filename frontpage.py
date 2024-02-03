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
        self.canvas = tk.Canvas(self.root, bg=col2)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        def create_header():
            banner = tk.Text(self.canvas, padx=10, pady=10, font = ("Oxygen", 30), bg=col3, relief="solid", borderwidth=2, wrap=tk.WORD, width=100, height=1)
            banner.pack()
            banner.insert(tk.END, "Title and organizers: ")
        
        def create_label(text1,x,y):
            text = ttk.Label(self.canvas,text=text1, background=col1, font=("Oxygen", 20))
            text.pack()


        self.objBox = self.canvas.create_rectangle(10, 110, 625, 475, outline="black", width=2)

        #banner
        self.banner = create_header()
        self.obj_label=create_label("Objectives",2,3)

        
        self.side = self.canvas.create_rectangle(1280, 80, 640, 800, outline="black", width=10)
        self.side.pack()

        





        #david's bottom 2 square
        self.root.mainloop()
        return


if __name__ == '__main__':
    Back()