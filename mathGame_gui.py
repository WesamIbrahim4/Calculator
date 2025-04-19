import tkinter as tk
import random

root = tk.Tk()
root.title("Math Game")
entry = tk.Entry(root, width=35, borderwidth= 5, font=("Arial", 14))
entry.grid(row=1, column=0, columnspan=4, padx=5, pady=10)

def evaluate():
    try:
        result = eval(entry.get())
        output = tk.Label(root,text= result)
        output.grid(row=3,column=2,pady=(10,0))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



tk.Button(root, text= "Enter", padx=40, pady=20 ,command=evaluate).grid(row = 3, column = 1)
    





label = tk.Label(root, text= "Create an equation with 3 numbers to reach the number",font= ("Arial",11,"bold"))
label.grid(row=0,column=0,columnspan=4,pady=(10,0))

randomNumber = random.randint(20,500)





root.mainloop()