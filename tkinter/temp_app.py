import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure(0, weight=1, minsize=50)
window.title("Temperature App")


def F_to_C():
    F = entry_temperature.get()
    C = (5 / 9) * (float(F) - 32)
    result_lbl["text"] = f"{round(C,2)} \N{DEGREE CELSIUS}"


entry_frm = tk.Frame(master=window)
entry_temperature = tk.Entry(master=entry_frm, width=10)
lbl_temp = tk.Label(master=entry_frm, text="\N{DEGREE FAHRENHEIT}")
entry_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=F_to_C
)
result_lbl = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

entry_frm.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
result_lbl.grid(row=0, column=2, padx=10)

window.mainloop()

