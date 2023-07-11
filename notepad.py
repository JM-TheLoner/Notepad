from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("920x510")
root.title("Notepad")
root.config(bg="lightblue")
root.resizable(False, False)

def save_file():
    open_file=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode="r", filetypes=[("text files", '*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)
    
b1 = Button(root, width="16", height="1", bg="white", text="Save File", command=save_file).place(x=300, y=5)
b2 = Button(root, width="16", height="1", bg="white", text="Open File", command=open_file).place(x=460, y=5)

entry = Text(root, width="113", height="29",wrap=WORD)
entry.place(x=6, y=35)

root.mainloop()