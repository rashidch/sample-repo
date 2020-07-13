import tkinter as tk

window = tk.Tk()
window.title("Real Python Tutorial")
"""
window.geometry("300x300")
entry = tk.Entry(fg="yellow", width=50, bg="black")
entry.pack()
usr_input = entry.get()
entry.insert(0, "Python")
#entry.delete(0)

text_box = tk.Text()
text_box.pack()
text_box.get(1.0,tk.END)
"""
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lable1 = tk.Label(master=frame1, text="I am at (0,0)")
lable1.place(x=0, y=0)
frame2 = tk.Frame(master=window, width=30, height=30, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lable2 = tk.Label(master=frame2, text="I am at (30,30)")
lable2.place(x=30, y=30)
frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lable3 = tk.Label(master=frame3, text="I am at (75,5)")
lable3.place(x=75, y=75)

window.mainloop()
