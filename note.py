import sys
import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
import logging # My debugger
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # this can disable the debugging
logging.debug('Start of program')

class Note:
    def __init__(self, window, box_colour, text=''):
        # Settings
        self.box_colour = box_colour
        background_colour = "steel blue"
        button_colour = "sky blue"

        # Window for new note
        self.window = window
        window.title("Cadmus Note")
        window.geometry("300x200")
        window.configure(bg=background_colour)

        window.rowconfigure(0, minsize=50, weight=1)
        window.rowconfigure(1, minsize=20, weight=0)
        window.columnconfigure(0, minsize=50, weight=1)

        # Variables
        self.is_stuck = False

        # Text edit window
        self.txt_edit = tk.Text(window, bg=self.box_colour)
        self.txt_edit.grid(row=0, column=0, sticky="nsew")
        self.txt_edit.insert(tk.END, text)

        # Frame for the buttons
        frm_buttons = tk.Frame(window)
        frm_buttons.grid(row=1, column=0)

        # Buttons for saving, sticking/unsticking and closing the note
        btn_save = tk.Button(frm_buttons, text="Save",
            bg=button_colour, command=self.save_note)
        btn_save.pack(side=tk.LEFT, expand=True, fill='both')
        btn_stick = tk.Button(frm_buttons, text="Stick",
            bg=button_colour, command=self.stick_note)
        btn_stick.pack(side=tk.LEFT, expand=True, fill='both')
        btn_close = tk.Button(frm_buttons, text="Close",
            bg=button_colour, command=self.close_note)
        btn_close.pack(side=tk.RIGHT, expand=True, fill='both')

    def close_note(self):
        """Close the window."""
        return self.window.destroy()

    def stick_note(self):
        """Remove the border of the note, making it look more like a sticky
        note, and vice versa!"""
        if self.is_stuck == False:
            self.is_stuck = True
            return self.window.overrideredirect(True)
        else:
            self.is_stuck = False
            return self.window.overrideredirect(False)

    def save_note(self):
        """Save the note"""
        file_this = asksaveasfilename(defaultextension="txt",
            filetypes=[("Text Files", "*.txt")])
        if not file_this:
            return
        with open(file_this, "w") as file_saved:
            text = self.txt_edit.get("1.0", tk.END)
            file_saved.write(text)

def main():
    window = tk.Tk()
    note_instance = Note(window, "purple")
    window.mainloop()

if __name__ == '__main__':
    main()