import tkinter as tk
from collections import deque

def colour_test():
    """Changes the colour of the text box based on the RGB values provided."""
    rgb_list = []
    for i in range(len(rgb)):
        if i == 0 or i % 2 == 0:
            continue
        else:
            rgb_list_item = int(rgb[i].get())
            rgb_list.append(rgb_list_item)
    rgb_string = _rbg_convert(rgb_list)
    print(rgb_string)
    txt_colour_check["bg"] = rgb_string
    return rgb_string

def _rbg_convert(rgb=[0, 0, 0]):
    """Translates an RBG tuple into a colour tkinter can work with."""
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

# Create main window and title it.
window = tk.Tk()
window.title("Cadmus")

window.columnconfigure(0, weight=1, minsize=200)
for i in range(10):
    window.rowconfigure(i, weight=1, minsize=25)

# Create colours frame and put it in the window
frm_colours = tk.Frame(master=window)
frm_colours.grid(row=4, column=0)
# Create a list for the colour labels and grids
rgb = []
# Create dictionary so correct colour is applied at the correct part of loop
rgb_text = deque(["Red", "Green", "Blue"])

# Loop for putting the colour labels and grids into the frame
for i in range(0, len(rgb_text)*2):
    if i == 0 or i % 2 == 0:
        rgb.append(tk.Label(master=frm_colours, text=rgb_text.popleft()))
        rgb[i].grid(row=0, column=i, sticky="e")
    else:
        zero = tk.StringVar()
        rgb.append(tk.Entry(master=frm_colours, width=5, textvariable=zero))
        rgb[i].grid(row=0, column=i, sticky="w")
        zero.set(0)

# Colours button frame
frm_colours_btn = tk.Frame(window)
frm_colours_btn.grid(row=5, column=0)
btn_apply_colour = tk.Button(
    frm_colours_btn,
    text="Check Colour",
    width=15,
    command=colour_test
)
btn_apply_colour.grid(row=0, column=0, pady=5)

# Colour test frame
txt_colour_check = tk.Text(frm_colours_btn, width=20, height=5)
txt_colour_check.grid(row=1, column=0)

# Main GUI loop
window.mainloop()