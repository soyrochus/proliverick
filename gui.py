#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""

import tkinter as tk
from tkinter import messagebox

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assessment Elements Generator")
        self.geometry('600x300')
        
        # Create a main frame
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Assessment Title
        self.label_title = tk.Label(main_frame, text="Assessment Title", anchor="w")
        self.label_title.grid(row=0, column=0, sticky="w")
        self.entry_title = tk.Entry(main_frame)
        self.entry_title.grid(row=0, column=1, sticky="we")
        
        # Elements Type
        self.label_type = tk.Label(main_frame, text="Elements Type", anchor="w")
        self.label_type.grid(row=1, column=0, sticky="w", pady=(20, 0))
        self.var_type = tk.StringVar(value="Open question")
        self.radio_open = tk.Radiobutton(main_frame, text="Open question", variable=self.var_type, value="Open question")
        self.radio_open.grid(row=1, column=1, sticky="w")
        self.radio_deduce = tk.Radiobutton(main_frame, text="Deduce the question", variable=self.var_type, value="Deduce the question")
        self.radio_deduce.grid(row=2, column=1, sticky="w")
        
        # Number of Elements
        self.label_number = tk.Label(main_frame, text="Number of Elements", anchor="w")
        self.label_number.grid(row=3, column=0, sticky="w", pady=(20, 0))
        self.var_number = tk.IntVar(value=1)
        self.option_number = tk.OptionMenu(main_frame, self.var_number, *range(1, 17))
        self.option_number.grid(row=3, column=1, sticky="we")
        
        # Buttons
        self.button_cancel = tk.Button(main_frame, text="Cancel", command=self.destroy)
        self.button_cancel.grid(row=4, column=1, sticky="e", pady=20)
        self.button_ok = tk.Button(main_frame, text="OK", command=self.perform_action)
        self.button_ok.grid(row=4, column=2, sticky="e", padx=(0, 50), pady=20)
        
        # Configure the grid
        main_frame.columnconfigure(1, weight=1)
        
    def perform_action(self):
        title = self.entry_title.get()
        element_type = self.var_type.get()
        number_of_elements = self.var_number.get()
        data = {'title': title, 'element_type': element_type, 'number_of_elements': number_of_elements}
        print(data)
        self.destroy()

if __name__ == "__main__":
    app = Gui()
    app.mainloop()

        
    def perform_action(self):
        title = self.entry_title.get()
        element_type = self.var_type.get()
        selected_number = self.listbox_number.curselection()
        if not selected_number:
            messagebox.showerror("Error", "Please select a number of elements")
            return
        number_of_elements = int(self.listbox_number.get(selected_number[0]))
        data = {'title': title, 'element_type': element_type, 'number_of_elements': number_of_elements}
        print(data)  # For now, just print the data. Later, you can replace this with the actual function to generate the assessment elements.
        self.destroy()

if __name__ == "__main__":
    app = Gui(tk.Tk)
    app.mainloop()