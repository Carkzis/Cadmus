import tkinter as tk
from tkinter import font
from collections import deque
from playsound import playsound
import random

def colour_test():
    """Changes the colour of the text box based on the RGB values provided."""
    rgb_list = []
    # Only odd numbers have the rgb value, so skip 0 and evens
    for i in range(len(rgb)):
        if i == 0 or i % 2 == 0:
            continue
        else:
            rgb_list_item = int(rgb[i].get())
            # Only allow valid rgb values
            if rgb_list_item > 255 or rgb_list_item < 0:
                print("Invalid colour!")
                return
            rgb_list.append(rgb_list_item)
    # Return function call to convert rgb list into a format tkinter can use
    # Change colour of colour text box
    return _rbg_convert(rgb_list)

def random_colour():
    """Puts a random colour in the text box."""
    rgb_list = []
    # Assign random colour numbers from 0 to 255 inclusive and add to list
    # Bit of a long way of taking the list of colour label/entry pairs and
    # dividing by two, forgot popping the deque removes items from rgb_text!
    for i in range(int(len(rgb)/2)):
        print(i)
        rand_colour_num = random.randint(0, 255)
        rgb_list.append(rand_colour_num)
    # Call function to convert rgb list into a format tkinter can use
    rgb_string = _rbg_convert(rgb_list)
    txt_colour_check["bg"] = rgb_string
    # Return function call to convert rgb list into a format tkinter can use
    # Change colour of colour text box
    return _rbg_convert(rgb_list)

def _rbg_convert(rgb=[0, 0, 0]):
    """Translates an RBG tuple into a colour tkinter can work with."""
    r, g, b = rgb
    txt_colour_check["bg"] = f'#{r:02x}{g:02x}{b:02x}'
    return txt_colour_check["bg"]

# Create main window and title it.
window = tk.Tk()
window.geometry("300x400") # set window size from the start
window.title("Cadmus")
window.resizable(0, 0) # Don't allow resizing

window.columnconfigure(0, weight=1, minsize=200)
for i in range(10):
    window.rowconfigure(i, weight=1, minsize=25)

# Create big label for title
lbl_title = tk.Label(
    text="CADMUS",
    fg="purple", # sets the text colour
)
font_tuple = ("Comic Sans MS", 30, "bold")
lbl_title.configure(font=font_tuple)
lbl_title.grid(row=0, column=0)

# Create colours frame and put it in the window
frm_colours = tk.Frame(master=window)
frm_colours.grid(row=4, column=0)
# Create a list for the colour labels and grids
rgb = []
# Create dictionary so correct colour is applied at the correct part of loop
rgb_text = deque(["Red", "Green", "Blue"])

# Loop for putting the colour labels and grids into the frame
for i in range(0, len(rgb_text)*2):
    # Zero and even numbers will be labels, odds will be entry boxes for
    # the rbg values, these get added to a list
    if i == 0 or i % 2 == 0:
        rgb.append(tk.Label(master=frm_colours, text=rgb_text.popleft()))
        rgb[i].grid(row=0, column=i, sticky="se")
    else:
        # Set initial values for the entry boxes to zero
        zero = tk.StringVar()
        rgb.append(tk.Entry(master=frm_colours, width=5, textvariable=zero))
        rgb[i].grid(row=0, column=i, sticky="sw")
        zero.set(0)

# Colours button frame
frm_colours_btn = tk.Frame(window)
frm_colours_btn.grid(row=5, column=0)
# Defined colour
btn_apply_colour = tk.Button(
    frm_colours_btn,
    text="Choose Colour",
    width=15,
    command=colour_test
)
btn_apply_colour.grid(row=0, column=0, pady=5, padx=1)
#Random colour
btn_rand_colour = tk.Button(
    frm_colours_btn,
    text="Random Colour",
    width=15,
    command=random_colour
)
btn_rand_colour.grid(row=0, column=1, pady=5, padx=1)

# Colour test output frame
txt_colour_check = tk.Text(frm_colours_btn, width=20, height=5)
txt_colour_check.grid(row=1, column=0, columnspan=2, sticky="ew")

# Soundboard frame
frm_sounds = tk.Frame(window)
frm_sounds.grid(row=6, column=0)
snd_f = lambda: playsound(
    random.choice(['cow.mp3', 'cow2.mp3', 'cow3.mp3', 'cow4.mp3', 'cow5.mp3'])
)

# Button to play random cow noise
btn_moo = tk.Button(
    frm_sounds,
    text="Moo?",
    width=15,
    command=snd_f
)
btn_moo.grid(row=0, column=0, pady=5)

# Main GUI loop
window.mainloop()