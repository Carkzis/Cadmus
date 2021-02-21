import sys
import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
import logging # My debugger
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # this can disable the debugging
logging.debug('Start of program')

def close_note():
    """Close the window."""
    return sys.exit()

def stick_note():
    """Remove the border of the note, making it look more like a sticky
    note, and vice versa!"""
    global is_stuck
    if is_stuck == False:
        is_stuck = True
        return window.overrideredirect(True)
    else:
        is_stuck = False
        return window.overrideredirect(False)

def save_note():
    """Save the note"""
    file_this = asksaveasfilename(defaultextension="txt",
        filetypes=[("Text Files", "*.txt")])
    if not file_this:
        return
    with open(file_this, "w") as file_saved:
        text = txt_edit.get("1.0", tk.END)
        file_saved.write(text)

# Settings
background_colour = "steel blue"
button_colour = "sky blue"

# Window for new note
window = tk.Tk()
window.title("Cadmus Note")
window.geometry("300x200")
window.configure(bg=background_colour)

window.rowconfigure(0, minsize=50, weight=1)
window.rowconfigure(1, minsize=20, weight=0)
window.columnconfigure(0, minsize=50, weight=1)

# Variables
is_stuck = False

# Text edit window
txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=0, sticky="nsew")

# Frame for the buttons
frm_buttons = tk.Frame(window)
frm_buttons.grid(row=1, column=0)

# Buttons for saving, sticking/unsticking and closing the note
btn_save = tk.Button(frm_buttons, text="Save",
    bg=button_colour, command=save_note)
btn_save.pack(side=tk.LEFT, expand=True, fill='both')
btn_stick = tk.Button(frm_buttons, text="Stick",
    bg=button_colour, command=stick_note)
btn_stick.pack(side=tk.LEFT, expand=True, fill='both')
btn_close = tk.Button(frm_buttons, text="Close",
    bg=button_colour, command=close_note)
btn_close.pack(side=tk.RIGHT, expand=True, fill='both')

window.update()
window.mainloop()