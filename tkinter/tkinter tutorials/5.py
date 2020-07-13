import tkinter as tk



master = tk.Tk()
v = tk.IntVar()
v.set(0)
master.title("Choose Language")

def ShowChoice():
    label = tk.Label(master,text="Choice\n"+str(v.get()),font=('Arial', 13)).pack(side="right")
languages = [("Python",1), ("Perl",2), ("Jave", 3), ("C++",4), ("C",5)]

tk.Label(master, text= "Choose a programming language", justify = tk.LEFT, padx = 20).pack()
for val, language in enumerate(languages):
    tk.Radiobutton(master, text=language, indicatoron=0, padx=20, width=20, variable=v, command=ShowChoice, value=val).pack(anchor=tk.W)

master.mainloop()

