import tkinter as tk

# Create main window and title it.
window = tk.Tk()
window.title("Cadmus")

window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(0, minsize=300, weight=1)

# Create colours frame and put it in the window
frm_colours = tk.Frame(master=window)
frm_colours.grid(row=0, column=0)
# Create a list for the colour labels and grids
rgb = []
# Create dictionary so correct colour is applied at the correct part of loop
rgb_text = {0: "Red:", 2: "Green:", 4: "Blue:"}

# Loop for putting the colour labels and grids into the frame
for i in range(0, 6):
    if i == 0 or i % 2 == 0:
        rgb.append(tk.Label(master=frm_colours, text=rgb_text[i]))
        rgb[i].grid(row=0, column=i, sticky="e")
    else:
        rgb.append(tk.Entry(master=frm_colours, width=5))
        rgb[i].grid(row=0, column=i, sticky="w")

# Main GUI loop
window.mainloop()