import tkinter as tk

master = tk.Tk()
master.title("Choose Your Gender")
master.geometry("300x300")
def var_states():
    print("male:{0} female:{1}".format(var1.get(),var2.get()))
var1 = tk.IntVar()
tk.Checkbutton(master, text = "male", variable=var1, font= "Arial", padx= 10, pady=5).grid(row=0,sticky=tk.W)
var2 = tk.IntVar()
tk.Checkbutton(master, text ="female", variable=var2,font= "Arial", padx= 10, pady=5).grid(row=1, sticky=tk.W)
tk.Button(master, text="Quit", width = 10, command=quit).grid(row=3, sticky=tk.W, padx=10, pady=5)
tk.Button(master, text="Show", width=10,  command=var_states).grid(row=4, sticky=tk.W, padx=10, pady=5)
tk.mainloop()
