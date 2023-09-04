#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import tkinter.filedialog
from proliverick.assesements import create_assesement

class Gui(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")
        self.title("Assessment Elements Generator")
        self.geometry('800x400')
        self.configure(bg=self.tk.eval('ttk::style lookup TFrame -background'))
        

        # Create a main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Assessment Title
        self.label_title = ttk.Label(main_frame, text="Assessment Title", anchor="w")
        self.label_title.grid(row=0, column=0, sticky="w")
        self.entry_title = ttk.Entry(main_frame)
        self.entry_title.grid(row=0, column=1, sticky="we")
        
        # Elements Type
        self.label_type = ttk.Label(main_frame, text="Elements Type", anchor="w")
        self.label_type.grid(row=1, column=0, sticky="w", pady=(20, 0))
        self.var_type = tk.StringVar(value="Reverse interrogation")
        self.radio_open = ttk.Radiobutton(main_frame, text="Reverse interrogation", variable=self.var_type, value="Open question")
        self.radio_open.grid(row=1, column=1, sticky="w")
        self.radio_deduce = ttk.Radiobutton(main_frame, text="Deduce the question", variable=self.var_type, value="Deduce the question")
        self.radio_deduce.grid(row=2, column=1, sticky="w")
        
        # Number of Elements
        self.label_number = ttk.Label(main_frame, text="Number of Elements", anchor="w")
        self.label_number.grid(row=3, column=0, sticky="w", pady=(20, 0))
        self.var_number = tk.IntVar(value=1)
        self.option_number = ttk.OptionMenu(main_frame, self.var_number, *range(1, 17))
        self.option_number.grid(row=3, column=1, sticky="we")
        
        # Output File Type
        self.label_file_type = ttk.Label(main_frame, text="Output File Type", anchor="w")
        self.label_file_type.grid(row=4, column=0, sticky="w", pady=(20, 0))
        self.var_file_type = tk.StringVar(value="Text")
        self.option_file_type = ttk.OptionMenu(main_frame, self.var_file_type, "Text", "Word document", "Excel sheet")
        self.option_file_type.grid(row=4, column=1, sticky="we")
        
        # Output File Path
        self.label_file_path = ttk.Label(main_frame, text="Output File Path", anchor="w")
        self.label_file_path.grid(row=5, column=0, sticky="w", pady=(20, 0))
        self.entry_file_path = ttk.Entry(main_frame)
        self.entry_file_path.grid(row=5, column=1, sticky="we")
        self.button_file_path = ttk.Button(main_frame, text="Browse", command=self.browse_file)
        self.button_file_path.grid(row=5, column=2, sticky="w")
        
        # Buttons
        self.button_cancel = ttk.Button(main_frame, text="Cancel", command=self.destroy)
        self.button_cancel.grid(row=6, column=2, sticky="e", pady=20)
        self.button_ok = ttk.Button(main_frame, text="OK", command=self.perform_action)
        self.button_ok.grid(row=6, column=1, sticky="e", pady=20, padx=(0, 10))
        
        # Configure the grid
        main_frame.columnconfigure(1, weight=1)
        
    def browse_file(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension="", 
                                                    filetypes=[("Text files", "*.txt"),
                                                               ("Word documents", "*.docx"),
                                                               ("Excel files", "*.xlsx"),
                                                               ("All files", "*.*")])
        self.entry_file_path.delete(0, tk.END)
        self.entry_file_path.insert(0, file_path)
        
    def perform_action(self):
        title = self.entry_title.get()
        element_type = self.var_type.get()
        number_of_elements = self.var_number.get()
        output_file_type = self.var_file_type.get()
        output_file_path = self.entry_file_path.get()
        data = {'title': title, 'element-type': element_type, 'number-of-elements': number_of_elements, 
            'output-file-type': output_file_type, 'output-file-path': output_file_path}
        print(data)  # For now, just print the data. Later, you can replace this with the actual function to generate the assessment elements.
        try:
            create_assesement(data)
        except Exception as e:
            messagebox.showerror("Error", str(e))   
            
        self.destroy()

