import tkinter as tk
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from collections import deque
from playsound import playsound
from note import Note
import random
import logging # My debugger
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # this can disable the debugging
logging.debug('Start of program')

class Main:

    def __init__(self, window):
        # Settings
        self.background_colour = "steel blue"
        self.button_colour = "sky blue"
        self.entry_colour = "sky blue"
        self.title_colour = "midnight blue"

        # Create main window and title it.
        self.window = window
        window.geometry("300x350") # set window size from the start
        window.title("Cadmus")
        window.configure(bg=self.background_colour)
        window.resizable(0, 0) # Don't allow resizing

        window.columnconfigure(0, weight=1, minsize=200)
        for i in range(7):
            window.rowconfigure(i, weight=1, minsize=25)

        # Create big label for title
        self.lbl_title = tk.Label(
            text="CADMUS",
            fg=self.title_colour, # sets the text colour
            bg=self.background_colour
        )
        self.font_tuple = ("Comic Sans MS", 30, "bold")
        self.lbl_title.configure(font=self.font_tuple)
        self.lbl_title.grid(row=0, column=0)

        # Create a button to create a new note
        self.btn_new_note = tk.Button(
            self.window,
            text="Create Note",
            width=15,
            bg=self.button_colour,
            command=self.create_new_note
        )
        self.btn_new_note.grid(row=1, column=0, pady=5, padx=1)

        # Create a button to load a sticky note
        self.btn_load_note = tk.Button(
            window,
            text="Load Note",
            width=15,
            bg=self.button_colour,
            command=self.load_note
        )
        self.btn_load_note.grid(row=2, column=0, pady=5, padx=1)

        # Create colours frame and put it in the window
        self.frm_colours = tk.Frame(master=window,
            bg=self.background_colour)
        self.frm_colours.grid(row=3, column=0)
        # Create a list for the colour labels and grids
        self.rgb = []
        # Create dictionary so correct colour is applied at the
        # correct part of loop
        self.rgb_text = deque(["Red", "Green", "Blue"])

        # Loop for putting the colour labels and grids into the frame
        for i in range(0, len(self.rgb_text)*2):
            # Zero and even numbers will be labels, odds will be entry boxes for
            # the rbg values, these get added to a list
            if i == 0 or i % 2 == 0:
                self.rgb.append(tk.Label(master=self.frm_colours,
                text=self.rgb_text.popleft(), bg=self.background_colour))
                self.rgb[i].grid(row=0, column=i, sticky="se")
            else:
                # Set initial values for the entry boxes to zero
                self.zero = tk.StringVar()
                self.rgb.append(tk.Entry(master=self.frm_colours, width=5,
                textvariable=self.zero, bg=self.entry_colour))
                self.rgb[i].grid(row=0, column=i, sticky="sw")
                self.zero.set(255)

        # Colours button frame
        self.frm_colours_btn = tk.Frame(window, bg=self.background_colour)
        self.frm_colours_btn.grid(row=4, column=0)
        # Defined colour
        self.btn_apply_colour = tk.Button(
            self.frm_colours_btn,
            text="Choose Colour",
            width=15,
            bg=self.button_colour,
            command=self.colour_test
        )
        self.btn_apply_colour.grid(row=0, column=0, pady=5, padx=1)
        #Random colour
        self.btn_rand_colour = tk.Button(
            self.frm_colours_btn,
            text="Random Colour",
            width=15,
            bg=self.button_colour,
            command=self.random_colour
        )
        self.btn_rand_colour.grid(row=0, column=1, pady=5, padx=1)

        # Colour test output frame
        self.txt_colour_check = tk.Text(self.frm_colours_btn,
            width=20, height=5)
        self.txt_colour_check.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Soundboard frame
        self.frm_sounds = tk.Frame(window, bg=self.background_colour)
        self.frm_sounds.grid(row=5, column=0)
        self.snd_f = lambda: playsound(
            random.choice(['cow.mp3', 'cow2.mp3', 'cow3.mp3', 'cow4.mp3',
                'cow5.mp3'])
        )

        # Button to play random cow noise
        self.btn_moo = tk.Button(
            self.frm_sounds,
            text="Moo?",
            width=15,
            bg=self.button_colour,
            command=self.snd_f
        )
        self.btn_moo.grid(row=0, column=0, pady=5)

    def colour_test(self):
        """Changes the colour of the text box based on the
        RGB values provided."""
        self.rgb_list = []
        # Only odd numbers have the rgb value, so skip 0 and evens
        for i in range(len(self.rgb)):
            if i == 0 or i % 2 == 0:
                continue
            else:
                self.rgb_list_item = int(self.rgb[i].get())
                # Only allow valid rgb values
                if self.rgb_list_item > 255 or self.rgb_list_item < 0:
                    print("Invalid colour!")
                    return
                self.rgb_list.append(self.rgb_list_item)
        # Return function call to convert rgb list into a format tkinter can use
        # Change colour of colour text box
        return self._rbg_convert(self.rgb_list)

    def random_colour(self):
        """Puts a random colour in the text box."""
        self.rgb_list = []
        # Assign random colour numbers from 0 to 255 inclusive and add to list
        # Bit of a long way of taking the list of colour label/entry pairs and
        # dividing by two, forgot popping the deque removes items from rgb_text!
        for i in range(int(len(self.rgb)/2)):
            self.rand_colour_num = random.randint(0, 255)
            self.rgb_list.append(self.rand_colour_num)
        # Call function to convert rgb list into a format tkinter can use
        self.rgb_string = self._rbg_convert(self.rgb_list)
        self.txt_colour_check["bg"] = self.rgb_string
        # Return function call to convert rgb list into a format tkinter can use
        # Change colour of colour text box
        return self._rbg_convert(self.rgb_list)

    def _rbg_convert(self, rgb_list=[255, 255, 255]):
        """Translates an RBG tuple into a colour tkinter can work with."""
        self.r, self.g, self.b = self.rgb_list
        self.txt_colour_check["bg"] = f'#{self.r:02x}{self.g:02x}{self.b:02x}'
        return self.txt_colour_check["bg"]

    def create_new_note(self):
        """Create a new note object."""
        self.new_note = tk.Toplevel(window)
        return Note(self.new_note, self.txt_colour_check["bg"])

    def load_note(self):
        """Open a file for editing."""
        self.this_file = askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if not self.this_file:
            return
        with open(self.this_file, "r") as self.read_file:
            self.new_note = tk.Toplevel(window)
            self.text = self.read_file.read()
        return Note(self.new_note, self.txt_colour_check["bg"], self.text)

def main():
    window = tk.Tk()
    main_instance = Main(window)
    window.mainloop()

if __name__ == '__main__':
    main()