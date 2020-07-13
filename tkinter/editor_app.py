import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
# window.geometry("800x800")
window.title("Text Editor")
window.rowconfigure(0, weight=1, minsize=600)
window.columnconfigure(1, weight=1, minsize=800)


def open_file():
    """ open a file for editing """
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")


def save_file():
    """save the current file as new file"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")


txt_edit = tk.Text(master=window)
fr_buttons = tk.Frame(master=window, relief=tk.GROOVE)
btn_open = tk.Button(
    master=fr_buttons, text="Open", command=open_file, width=10, height=3
)
btn_save = tk.Button(
    master=fr_buttons, text="Save As...", command=save_file, width=10, height=3
)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

