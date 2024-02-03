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
        self.mainframe = tk.Frame(self.root, background=col1)
        self.mainframe.pack(fill='both', expand=True)
        
        def create_header():
            banner = tk.Text(self.root, font = ('Oxygen', 16), bg="blue", pady=0, borderwidth=2, relief="solid", wrap=tk.WORD)
            banner.pack(pady=10)
            banner.insert(tk.END, "My Application Header")
        
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


# from tkinter import * 
# import tkinter as tk
# from tkinter.ttk import *

# class Box():

#     #width adn height predetermined
#     def __init__(self, root, title, x, y):

#         self.canvas = Canvas(root)
#         self.label = tk.Label(self.canvas, text = title, font = ('Helvetica',20))
#         self.canvas.pack()

#     def pack(self):
#         self.canvas.pack()
#         self.label

# root = tk.Tk()
# root.geometry("1920x1080")
# root.title("My second GUI I guess")
# label = tk.Label(root, text = "Hello World!", font=('Arial', 18)) #(part of root)
# label.pack(padx = 20, pady = 20)
# box = Box(root, "Test Box", 10,110)

# root.mainloop()

        
# root.geometry("1920x1080")
# root.title("My second GUI I guess")

# label = tk.Label(root, text = "Hello World!", font=('Arial', 18)) #(part of root)
# label.pack(padx = 20, pady = 20) # getting the label into the root using pack(padding)

                 

