from tkinter import *
from tkinter import ttk
import lets_play

root = Tk()
root.title("Gorillas - Gruppe 6")

# Mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Get Name for Player 1
name_1 = StringVar()
name_1_entry = ttk.Entry(mainframe, width=10, textvariable=name_1)
name_1_entry.grid(column=0, row=1)

# Get Name for Player 2
name_2 = StringVar()
name_2_entry = ttk.Entry(mainframe, width=10, textvariable=name_2)
name_2_entry.grid(column=1, row=1)

# Display Labels
ttk.Label(mainframe, text="Willkommen zu Gorillas\nPräsentiert von Gruppe 6").grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Player 1: ").grid(column=0, row=2)
ttk.Label(mainframe, text="Player 2: ").grid(column=1, row=2)


submit_button = ttk.Button(mainframe, text="Submit", command=lets_play)
submit_button.grid(column=0, row=3, columnspan=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", lets_play)
name_1_entry.focus()

root.mainloop()

