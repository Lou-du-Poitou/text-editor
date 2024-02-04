# Text Editor - Made by V / Lou du Poitou (c) 2024 - V.1 #

# --- --- --- #
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
import hashlib
# --- --- --- #

# --- --- --- #
app = tk.Tk()
app.title("V / Lou du Poitou - Text Editor")
app.geometry("428x460")
app.resizable(True, True)
app.overrideredirect(False)
try:
    app.iconbitmap(r"./icon.ico")
except:
    import sys
    app.iconbitmap(sys.executable)

app.config(background="#DEDEDE")
# --- --- --- #

# --- --- --- #
class variables:
    mode = True
    path = ""

def open_file():
    try:
        with open(filedialog.askopenfilename(defaultextension=".txt"), "r", encoding="utf-8") as file:
            text.config(state="normal")
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read().rstrip())
        if variables.mode == False:
            text.config(state="disabled")
        variables.path = file.name
        file.close()
    except:
        pass
    
def save_file():
    try: 
        with open(filedialog.asksaveasfilename(defaultextension=".txt"), "w", encoding="utf-8") as file:
            file.write(str(text.get("0.0", tk.END)))
        variables.path = file.name
        file.close()
    except:
        pass
    
def new_file():
    try:
        variables.path = ""
        variables.mode = True
        text_cmd.set("")
        text.config(state="normal")
        text.delete("1.0", tk.END)
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
        variables.mode = True
        text.config(state="normal")
        text.delete("1.0", tk.END)
    except:
        pass
    
def save():
    try:
        if variables.path != "":
            with open(variables.path, "w", encoding="utf-8") as file:
                file.write(str(text.get("0.0", tk.END)))
            file.close()
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
    
def message():
    try:
        if variables.path != "":
            messagebox.showinfo("Path :", variables.path)
    except:
        pass
# --- --- --- #

# --- --- --- #
btn1 = tk.Button(app, text="Open", height="1", width="8", bg="#DEDEDE", command=open_file, borderwidth="1", activebackground="#C6F9C7")
btn2 = tk.Button(app, text="Save", height="1", width="8", bg="#DEDEDE", command=save_file, borderwidth="1", activebackground="#C6F9C7")
btn3 = tk.Button(app, text="New", height="1", width="8", bg="#DEDEDE", command=new_file, borderwidth="1", activebackground="#C6F9C7")
btn4 = tk.Button(app, text="Mode", height="1", width="8", bg="#DEDEDE", command=change_mode, borderwidth="1", activebackground="#C6F9C7")
btn5 = tk.Button(app, text="Hash", height="1", width="8", bg="#DEDEDE", command=hash_file, borderwidth="1", activebackground="#C6F9C7")

clearbtn = tk.Button(app, text="✕", height="1", width="2", command=clear, bg="#D72020", borderwidth="1", activebackground="#C6F9C7")
savebtn = tk.Button(app, text="✓", height="1", width="2", command=save, bg="#20D720", borderwidth="1", activebackground="#C6F9C7")
windowbtn = tk.Button(app, text="↔", height="1", width="2", command=window, bg="#2020D7", borderwidth="1", activebackground="#C6F9C7")
hidebtn = tk.Button(app, text="", height="1", width="2", command=message, bg="#DEDEDE", borderwidth="1", activebackground="#C6F9C7")

text = tk.Text(app, bg="#ffffff", borderwidth="2", height="21", width="45", font=tkFont.Font(family="Arial", weight="normal"), undo=True)
text_cmd = tk.StringVar()
cmd = tk.Entry(app, width="43", borderwidth="2", textvariable=text_cmd, fg="#00A505", font=tkFont.Font(weight="bold"), state="readonly", justify="center")
scroll = tk.Scrollbar(app, bg="#DEDEDE", command=text.yview, orient="vertical", borderwidth="2", relief="sunken")

text["yscrollcommand"] = scroll.set

app.grid_propagate(False)
app.grid_rowconfigure(0, weight="1")
app.grid_columnconfigure(0, weight="1")

cmd.pack(side=tk.BOTTOM, expand=True, fill="x", padx="2", pady="2", anchor="s")

btn1.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
btn2.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
btn3.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
btn4.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
btn5.pack(side=tk.LEFT, expand=True, fill="x", pady="3")

savebtn.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
clearbtn.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
windowbtn.pack(side=tk.LEFT, expand=True, fill="x", pady="3")

text.grid(row="0", column="0", sticky=tk.NSEW, pady=30)
scroll.grid(row="0", column="1", sticky=tk.NSEW)
hidebtn.pack(side=tk.LEFT, expand=False, fill="x", pady="3")
# --- --- --- #

# --- --- --- #
app.mainloop()
# --- --- --- #

# Text Editor - Made by V / Lou du Poitou (c) 2024 - V.1 #
