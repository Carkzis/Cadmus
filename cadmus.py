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
        background_colour = "steel blue"
        button_colour = "sky blue"
        entry_colour = "sky blue"
        title_colour = "midnight blue"

        # Create main window and title it.
        self.window = window
        window.geometry("300x350") # set window size from the start
        window.title("Cadmus")
        window.configure(bg=background_colour)
        window.resizable(0, 0) # Don't allow resizing

        window.columnconfigure(0, weight=1, minsize=200)
        for i in range(7):
            window.rowconfigure(i, weight=1, minsize=25)

        # Create big label for title
        lbl_title = tk.Label(
            text="CADMUS",
            fg=title_colour, # sets the text colour
            bg=background_colour
        )
        font_tuple = ("Comic Sans MS", 30, "bold")
        lbl_title.configure(font=font_tuple)
        lbl_title.grid(row=0, column=0)

        # Create a button to create a new note
        btn_new_note = tk.Button(
            window,
            text="Create Note",
            width=15,
            bg=button_colour,
            command=self.create_new_note
        )
        btn_new_note.grid(row=1, column=0, pady=5, padx=1)

        # Create a button to load a sticky note
        btn_load_note = tk.Button(
            window,
            text="Load Note",
            width=15,
            bg=button_colour,
            command=self.load_note
        )
        btn_load_note.grid(row=2, column=0, pady=5, padx=1)

        # Create colours frame and put it in the window
        frm_colours = tk.Frame(master=window,
            bg=background_colour)
        frm_colours.grid(row=3, column=0)
        # Create a list for the colour labels and grids
        self.rgb = []
        # Create deque so correct colour is applied at the
        # correct part of loop
        rgb_text = deque(["Red", "Green", "Blue"])

        # Loop for putting the colour labels and grids into the frame
        for i in range(0, len(rgb_text)*2):
            # Zero and even numbers will be labels, odds will be entry boxes for
            # the rbg values, these get added to a list
            if i == 0 or i % 2 == 0:
                self.rgb.append(tk.Label(
                    master=frm_colours,
                    text=rgb_text.popleft(),
                    bg=background_colour
                    ))
                self.rgb[i].grid(row=0, column=i, sticky="se")
            else:
                # Set initial values for the entry boxes to zero
                zero = tk.StringVar()
                self.rgb.append(tk.Entry(master=frm_colours, width=5,
                textvariable=zero, bg=entry_colour))
                self.rgb[i].grid(row=0, column=i, sticky="sw")
                zero.set(255)

        # Colours button frame
        frm_colours_btn = tk.Frame(window, bg=background_colour)
        frm_colours_btn.grid(row=4, column=0)
        # Defined colour
        btn_apply_colour = tk.Button(
            frm_colours_btn,
            text="Choose Colour",
            width=15,
            bg=button_colour,
            command=self.colour_test
        )
        btn_apply_colour.grid(row=0, column=0, pady=5, padx=1)
        #Random colour
        btn_rand_colour = tk.Button(
            frm_colours_btn,
            text="Random Colour",
            width=15,
            bg=button_colour,
            command=self.random_colour
        )
        btn_rand_colour.grid(row=0, column=1, pady=5, padx=1)

        # Colour test output frame
        self.txt_colour_check = tk.Text(frm_colours_btn,
            width=20, height=5)
        self.txt_colour_check.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Soundboard frame
        frm_sounds = tk.Frame(window, bg=background_colour)
        frm_sounds.grid(row=5, column=0)
        self.snd_f = lambda: playsound(
            random.choice(['cow.mp3', 'cow2.mp3', 'cow3.mp3', 'cow4.mp3',
                'cow5.mp3'])
        )

        # Button to play random cow noise
        btn_moo = tk.Button(
            frm_sounds,
            text="Moo?",
            width=15,
            bg=button_colour,
            command=self.snd_f
        )
        btn_moo.grid(row=0, column=0, pady=5)

    def colour_test(self):
        """Changes the colour of the text box based on the
        RGB values provided."""
        rgb_list = []
        # Only odd numbers have the rgb value, so skip 0 and evens
        for i in range(len(self.rgb)):
            if i == 0 or i % 2 == 0:
                continue
            else:
                rgb_list_item = int(self.rgb[i].get())
                # Only allow valid rgb values
                if rgb_list_item > 255 or rgb_list_item < 0:
                    print("Invalid colour!")
                    return
                rgb_list.append(rgb_list_item)
        # Return function call to convert rgb list into a format tkinter can use
        # Change colour of colour text box
        return self._rbg_convert(rgb_list)

    def random_colour(self):
        """Puts a random colour in the text box."""
        rgb_list = []
        # Assign random colour numbers from 0 to 255 inclusive and add to list
        # Bit of a long way of taking the list of colour label/entry pairs and
        # dividing by two, forgot popping the deque removes items from rgb_text!
        for i in range(int(len(self.rgb)/2)):
            rand_colour_num = random.randint(0, 255)
            rgb_list.append(rand_colour_num)
        # Call function to convert rgb list into a format tkinter can use
        rgb_string = self._rbg_convert(rgb_list)
        self.txt_colour_check["bg"] = rgb_string
        # Return function call to convert rgb list into a format tkinter can use
        # Change colour of colour text box
        return self._rbg_convert(rgb_list)

    def _rbg_convert(self, rgb_list=[255, 255, 255]):
        """Translates an RBG tuple into a colour tkinter can work with."""
        r, g, b = rgb_list
        self.txt_colour_check["bg"] = f'#{r:02x}{g:02x}{b:02x}'
        return self.txt_colour_check["bg"]

    def create_new_note(self):
        """Create a new note object."""
        new_note = tk.Toplevel(self.window)
        return Note(new_note, self.txt_colour_check["bg"])

    def load_note(self):
        """Open a file for editing."""
        this_file = askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if not this_file:
            return
        with open(this_file, "r") as read_file:
            new_note = tk.Toplevel(self.window)
            text = read_file.read()
        return Note(new_note, self.txt_colour_check["bg"], text)

def main():
    window = tk.Tk()
    main_instance = Main(window)
    window.mainloop()

if __name__ == '__main__':
    main()
