import tkinter as tk

root = tk.Tk()
root.title("Tkinter Tutorial")
root.geometry('800x400')
frame = tk.Frame(root).pack() 
widget =tk.Label(root, text="The tech guy").pack(side='right')

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

#tk.Label(root, justify=tk.LEFT, padx = 20, text= explanation).pack(side= 'left')
#tk.Label(root,text="Red text in times font", fg="red", font="Times").pack()
#tk.Label(root, text= "Green text in Helvetica font", fg="light green", font="Helvetica 16 bold italic").pack()
#tk.Label(root, text=" Blue Text", fg="blue", font="Verdana 10 bold").pack()
tk.Button(root, text= 'Stop', width= 25, command = root.destroy).pack(side= "left")
tk.Message(root, anchor="w", relief= "sunken", padx="20", pady="50",text= explanation).pack()

def write_slogan():
    print("Tkniter is easy to use!")

tk.Button(frame, text= "QUIT", anchor='center', fg= "red", command=quit).pack()
tk.Button(frame, text="Hello", command="write_slogan").pack()

root.mainloop()



