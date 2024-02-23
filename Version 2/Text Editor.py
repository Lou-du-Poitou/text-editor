# Text Editor - Made by V / Lou du Poitou (c) 2024 - V.2 #
## Vencryption (c) 2024 - Made by V / Lou du Poitou ##
##
# GitHub => https://github.com/Lou-du-Poitou/
# Python => https://pypi.org/user/lou_du_poitou/
# Link => https://encryption.nexcord.pro/
##

# --- --- --- #
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
import hashlib
import vencryption
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
    crypt = False
    key = "0000000000000000"

def open_file(path:str=None):
    try:
        if path != None:
            with open(path, "r", encoding="utf-8") as file:
                text.config(state="normal")
                text.delete("1.0", tk.END)
                text.insert(tk.END, file.read().rstrip())
            variables.path = file.name
            text_cmd.set("")
            file.close()
            ## CLEAR VARIABLES ##
            del path, file
        else:
            path = filedialog.askopenfilename(defaultextension=".txt")
            if variables.crypt == False:
                with open(path, "r", encoding="utf-8") as file:
                    text.config(state="normal")
                    text.delete("1.0", tk.END)
                    text.insert(tk.END, file.read().rstrip())
                if variables.mode == False:
                    text.config(state="disabled")
                variables.path = file.name
                text_cmd.set("")
                file.close()
                ## CLEAR VARIABLES ##
                del path, file
            else:
                with open(path, "rb") as file:
                    content = vencryption.decrypt(file.read(), variables.key).decode().rstrip()
                    text.config(state="normal")
                    text.delete("1.0", tk.END)
                    text.insert(tk.END, content)
                if variables.mode == False:
                    text.config(state="disabled")
                variables.path = file.name
                text_cmd.set("")
                file.close()
                ## CLEAR VARIABLES ##
                del path, file, content
    except:
        if path:
            messagebox.showerror("Error :", f"Failed to open this file !")
            new_file()
        ## CLEAR VARIABLES ##
        del path
    
def save_file():
    try: 
        if variables.crypt == False:
            with open(filedialog.asksaveasfilename(defaultextension=".txt"), "w", encoding="utf-8") as file:
                file.write(str(text.get("0.0", tk.END)))
            variables.path = file.name
            file.close()
            ## CLEAR VARIABLES ##
            del file
        else:
            with open(filedialog.asksaveasfilename(defaultextension=".txt"), "wb") as file:
                content = vencryption.crypt(text.get("0.0", tk.END).encode(), variables.key)
                file.write(content)
            variables.path = file.name
            file.close()
            ## CLEAR VARIABLES ##
            del file, content
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
    
def save():
    try:
        if variables.path != "":
            if variables.crypt == False:
                with open(variables.path, "w", encoding="utf-8") as file:
                    file.write(str(text.get("0.0", tk.END)))
                file.close()
                ## CLEAR VARIABLES ##
                del file
            else:
                with open(variables.path, "wb") as file:
                    content = vencryption.crypt(text.get("0.0", tk.END).encode(), variables.key)
                    file.write(content)
                file.close()
                ## CLEAR VARIABLES ##
                del file, content
        else:
            messagebox.showwarning("Warn :", "Cannot save a non-existent file !")
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
            content = e.read()
            hash = hashlib.md5(content.encode(), usedforsecurity=True).hexdigest()
            if hash == text_cmd.get():
                hash = vencryption.getHach(content)
        e.close()
        text_cmd.set(hash)
        ## CLEAR VARIABLES ##
        del e, content, hash
    except:
        pass
    
def message():
    try:
        if variables.path != "":
            messagebox.showinfo("Path :", variables.path)
    except:
        pass
    
def options():
    try:
        for i in app.winfo_children():
            if isinstance(i, tk.Toplevel):
                i.destroy()
                
        # --- --- --- #
        
        win = tk.Toplevel(app)
        win.title("Options")
        win.geometry("300x120")
        win.resizable(False, False)
        win.iconbitmap(sys.executable)
        win.attributes("-topmost", True)
        win.grab_set()
        
        # --- --- --- #
        
        def setCrypt():
            if variables.crypt == True:
                variables.crypt = False
                cryptOrNotBtn.configure(background="#00ff00")
            elif variables.crypt == False:
                variables.crypt = True
                cryptOrNotBtn.configure(background="#ff0000")
                
        def setKey():
            e = keyVariable.get()
            if e.strip() != "" and e.strip() != variables.key:
                variables.key = e
                win.destroy()
            ## CLEAR VARIABLES ##
            del e
                
        # --- --- --- #

        keyVariable = tk.StringVar()
        keyVariable.set(variables.key)
        if variables.crypt == False:
            cryptOrNotBtn = tk.Button(win, text="MODE CRYPTAGE", height="1", background="#20D720", command=setCrypt, borderwidth="3", activebackground="#C6F9C7", font=tkFont.BOLD)
        else:
            cryptOrNotBtn = tk.Button(win, text="MODE CRYPTAGE", height="1", background="#D72020", command=setCrypt, borderwidth="3", activebackground="#C6F9C7", font=tkFont.BOLD)
        setKeyInput = tk.Entry(win, width="20", borderwidth="2", textvariable=keyVariable, font=tkFont.Font(weight="bold", size="13"), justify=tk.CENTER)
        setKeyBtn = tk.Button(win, text="ENREGISTRER CLÉ", height="1", background="#D7D720", command=setKey, borderwidth="3", activebackground="#C6F9C7", font=tkFont.BOLD)
        
        # --- --- --- #
        
        setKeyBtn.pack(side=tk.BOTTOM, expand=True, fill="x", padx="5", pady="5")
        setKeyInput.pack(side=tk.BOTTOM, expand=True, fill="x", padx="5", pady=("5", "0"))
        cryptOrNotBtn.pack(side=tk.BOTTOM, expand=True, fill="x", padx="5", pady="5")
    except:
        pass
# --- --- --- #

# --- --- --- #
btn1 = tk.Button(app, text="Open", height="1", width="8", bg="#DEDEDE", command=open_file, borderwidth="1", activebackground="#C6F9C7")
btn2 = tk.Button(app, text="Save", height="1", width="8", bg="#DEDEDE", command=save_file, borderwidth="1", activebackground="#C6F9C7")
btn3 = tk.Button(app, text="New", height="1", width="8", bg="#DEDEDE", command=new_file, borderwidth="1", activebackground="#C6F9C7")
btn4 = tk.Button(app, text="Mode", height="1", width="8", bg="#DEDEDE", command=change_mode, borderwidth="1", activebackground="#C6F9C7")
btn5 = tk.Button(app, text="Hash", height="1", width="8", bg="#DEDEDE", command=hash_file, borderwidth="1", activebackground="#C6F9C7")

savebtn = tk.Button(app, text="✓", height="1", width="2", command=save, bg="#20D720", borderwidth="1", activebackground="#C6F9C7")
optionsbtn = tk.Button(app, text="ⓥ", height="1", width="2", command=options, bg="#D7D720", borderwidth="1", activebackground="#C6F9C7")
windowbtn = tk.Button(app, text="↔", height="1", width="2", command=window, bg="#2020D7", borderwidth="1", activebackground="#C6F9C7")
hidebtn = tk.Button(app, text="", height="1", width="2", command=message, bg="#DEDEDE", borderwidth="1", activebackground="#C6F9C7")

text = tk.Text(app, bg="#ffffff", borderwidth="2", height="21", width="45", font=tkFont.Font(family="Arial", weight="normal", size="13"), undo=True)
text_cmd = tk.StringVar()
cmd = tk.Entry(app, width="43", borderwidth="2", textvariable=text_cmd, fg="#00A505", font=tkFont.Font(weight="bold", size="13"), state="readonly", justify="center")
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
optionsbtn.pack(side=tk.LEFT, expand=True, fill="x", pady="3")
windowbtn.pack(side=tk.LEFT, expand=True, fill="x", pady="3")

text.grid(row="0", column="0", sticky=tk.NSEW, pady=30)
scroll.grid(row="0", column="1", sticky=tk.NSEW)
hidebtn.pack(side=tk.LEFT, expand=False, fill="x", pady="3")
# --- --- --- #

## OPEN FILE IN APP ##
from sys import argv
try:
    script, file = argv
    open_file(file)
    ## CLEAR VARIABLES ##
    del script, file
except:
    pass
## --- --- --- --- ##

# --- --- --- #
app.mainloop()
# --- --- --- #

# Text Editor - Made by V / Lou du Poitou (c) 2024 - V.2 #
## Vencryption (c) 2024 - Made by V / Lou du Poitou ##
