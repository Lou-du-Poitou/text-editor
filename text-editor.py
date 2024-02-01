# Text Editor - Made by V / Lou du Poitou (c) 2024 - V.1 #

# --- --- --- #
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import hashlib
# --- --- --- #

# --- --- --- #
app = tk.Tk()
app.title("V / Lou du Poitou - Text Editor")
app.geometry("428x450")
app.resizable(False, False)
app.overrideredirect(False)
try:
    app.iconbitmap(r"./icon.ico")
except:
    pass
# --- --- --- #

# --- --- --- #
class variables:
    mode = True
    path = ""

def open_file():
    try:
        file = filedialog.askopenfile(mode="r", defaultextension=".txt")
        if file:
            text.config(state="normal")
            text.delete("1.0", tk.END)
            text.insert(tk.END, str(file.read()).rstrip())
        if variables.mode == False:
            text.config(state="disabled")
        variables.path = file.name
        file.close()
    except:
        pass
    
def save_file():
    try:
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        file.write(str(text.get("0.0", tk.END)))
        variables.path = file.name
        file.close()
    except:
        pass
    
def new_file():
    try:
        text.config(state="normal")
        text.delete("1.0", tk.END)
        variables.path = ""
    except:
        pass
    
def change_mode():
    try:
        if variables.mode == True:
            text.config(state="disabled")
            variables.mode = False
        else:
            text.config(state="normal")
            variables.mode = True
    except:
        pass
    
def clear():
    try:
        variables.path = ""
        variables.mode = True
        text_cmd.set("")
        text.config(state="normal")
        text.delete("1.0", tk.END)
    except:
        pass
    
def save():
    try:
        if variables.path != "":
            with open(variables.path, "w") as e:
                e.write(str(text.get("0.0", tk.END)))
            e.close()
    except:
        pass
    
def window():
    try:
        if app.attributes("-topmost"):
            app.attributes("-topmost", False)
        else:
            app.attributes("-topmost", True)
    except:
        pass
    
def hash_file():
    try:
        with open(variables.path, "r") as e:
            hash = hashlib.md5(e.read().encode(), usedforsecurity=True).hexdigest()
        text_cmd.set(hash)
    except:
        pass
# --- --- --- #

# --- --- --- #
btn1 = tk.Button(app, text="Open", height="1", width="8", bg="#DEDEDE", command=open_file)
btn1.place(x=0, y=0)

btn2 = tk.Button(app, text="Save", height="1", width="8", bg="#DEDEDE", command=save_file)
btn2.place(x=66, y=0)

btn3 = tk.Button(app, text="New", height="1", width="8", bg="#DEDEDE", command=new_file)
btn3.place(x=132, y=0)

btn4 = tk.Button(app, text="Mode", height="1", width="8", bg="#DEDEDE", command=change_mode)
btn4.place(x=198, y=0)

btn5 = tk.Button(app, text="Hash", height="1", width="8", bg="#DEDEDE", command=hash_file)
btn5.place(x=264, y=0)

exitbtn = tk.Button(app, text="✕", height="1", width="2", command=clear, bg="#ff0000")
exitbtn.place(x=358, y=0)

savebtn = tk.Button(app, text="✓", height="1", width="2", command=save, bg="#00ff00")
savebtn.place(x=332, y=0)

windowbtn = tk.Button(app, text="↔", height="1", width="2", command=window, bg="#0000ff")
windowbtn.place(x=384, y=0)

text = tk.Text(app, bg="#ffffff", borderwidth="2", height="21", width="45", font=tkFont.Font(family="Arial", weight="normal"))
text.place(x=0, y=25)

text_cmd = tk.StringVar()

cmd = tk.Entry(app, width="43", borderwidth="2", textvariable=text_cmd, fg="#00A505", font=tkFont.Font(weight="bold"), state="readonly", justify="center")
cmd.place(x=9, y=421)

scroll = tk.Scrollbar(app, command=text.yview, orient="vertical", borderwidth="2")

text["yscrollcommand"] = scroll.set

text.pack(fill=tk.NONE, expand=False, side=tk.LEFT)
scroll.pack(fill=tk.Y, expand=True, side=tk.RIGHT)
# --- --- --- #

# --- --- --- #
app.mainloop()
# --- --- --- #

# Text Editor - Made by V / Lou du Poitou (c) 2024 - V.1 #
