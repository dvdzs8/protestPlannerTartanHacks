TK_SILENCE_DEPRECATION=1

import tkinter as tk

root = tk.Tk()

root.geometry("200x200")
root.title("My second GUI I guess")

label = tk.Label(root, text = "Hello World!", font=('Arial', 18)) #(part of root)
label.pack(padx = 20, pady = 20) # getting the label into the root using pack(padding)


textbox = tk.Text(root, font = ('Oxygen', 16))
textbox.pack()

myEntry = tk.Entry(root)
myEntry.pack()

btn = tk.Button(root, text = "Click", font = ("Oxygen", 18))
btn.pack(padx = 100, pady = 50)

btnFrame = tk.Frame(root)
btnFrame.columnconfigure(0, weight = 1)
btnFrame.columnconfigure(1, weight = 1)
btnFrame.columnconfigure(2, weight = 1)

btn1 = tk.Button(btnFrame, text = "1")
btn1.grid(row =0 , column = 0, sticky  = "we")

btn2 = tk.Button(btnFrame, text = "1")
btn2.grid(row =0 , column = 1, sticky  = "we")

btn3 = tk.Button(btnFrame, text = "1")
btn3.grid(row =1 , column = 0, sticky  = "we")

btn4 = tk.Button(btnFrame, text = "1")
btn4.grid(row =1 , column = 1, sticky  = "we")

btnFrame.pack(fill ="x")

root.mainloop()