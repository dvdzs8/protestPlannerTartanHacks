import tkinter as tk
from tkinter import ttk
from contacts import signups

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
            banner.insert(tk.END, "Title and Organizers: ")
        
        def create_label(text1,x,y):
            text = ttk.Label(self.canvas,text=text1, background=col1, font=("Oxygen", 20))
            text.pack()

        self.objBox = self.canvas.create_rectangle(10, 100, 635, 400, outline="black", width=2)
        self.objTitle = tk.Label(self.canvas, text = "Objectives", font=('Oxygen', 18))
        self.objTitle.place(x = 20, y = 120)
        self.obj1 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.obj1.place(x = 20, y = 165)
        self.obj2 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.obj2.place(x = 20, y = 250)
        self.obj3 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.obj3.place(x = 20, y = 335)

        self.contactBox = self.canvas.create_rectangle(10, 450, 635, 750, outline="black", width=2)
        self.conTitle = tk.Label(self.canvas, text = "Contacts", font=('Oxygen', 18))
        self.conTitle.place(x = 20, y = 470)
        self.con1 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.con1.place(x = 20, y = 515)
        self.con2 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.con2.place(x = 20, y = 600)
        self.con3 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.con3.place(x = 20, y = 685)

        self.locBox = self.canvas.create_rectangle(645, 100, 1270, 400, outline="black", width=2)
        self.locTitle = tk.Label(self.canvas, text = "Location", font=('Oxygen', 18))
        self.locTitle.place(x = 665, y = 120)
        self.locText = tk.Text(self.canvas, font = ("Oxygen", 14))
        self.locText.place(x = 665, y = 160, width = 580, height = 220)

        self.dateBox = self.canvas.create_rectangle(645, 450, 1270, 750, outline="black", width=2)
        self.dateTitle = tk.Label(self.canvas, text = "Key Dates", font=('Oxygen', 18))
        self.dateTitle.place(x = 665, y = 470)
        self.date1 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.date1.place(x = 665, y = 515)
        self.date2 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.date2.place(x = 665, y = 600)
        self.date3 = tk.Entry(self.canvas, font =("Oxygen", 14), width = 53)
        self.date3.place(x = 665, y = 685)

        #banner
        self.banner = create_header()
        

        #side panel
        self.canvas.create_rectangle(1000, 100, 1500, 900, outline="black", width=5)


        #sign ups

        # Create a button
        self.signTitle = tk.Label(self.canvas, text = "Sign up!", font=('Oxygen', 18))
        self.signTitle.place(x = 1050, y = 130)
        name = ttk.Entry(self.root)
        label = tk.Label(self.root, text="Name:")
        label_window=self.canvas.create_window(1050,180, anchor=tk.NW, window=label)
        input_window = self.canvas.create_window(1200,180, anchor=tk.NW, window=name)
        
        # Place the button on the canvas at coordinates (50, 50)
        
        # Create a label for displaying messages

        email = ttk.Entry(self.root)
        label_e = tk.Label(self.root, text="Email:")
        label_window_e=self.canvas.create_window(1050,230, anchor=tk.NW, window=label_e)
        input_window_e = self.canvas.create_window(1200,230, anchor=tk.NW, window=email)

        button = tk.Button(self.canvas, text="Done!", command=signups(name.get(),email.get()))
        button_window = self.canvas.create_window(1300, 300, anchor=tk.NW, window=button)

        #david's bottom 2 square
        self.root.mainloop()
        return


if __name__ == '__main__':
    Back()