import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f" Row {i} \n colomn{j}")
        label.pack(padx=5, pady=5)


events_list = []


def handle_keypress(event):
    print(event.char)


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("The button was clicked!")


window.mainloop()
