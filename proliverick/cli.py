#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""
import argparse
from proliverick.assesements import create_assesement
from proliverick.gui import Gui

def perform_action_cli(args):
    data = {'title': args.title, 'element-type': args.element_type, 'number-of-elements': args.number_of_elements, 
            'output-file-type': args.output_file_type, 'output-file-path': args.output_file_path}
    try:
        create_assesement(data)
        print(f"File written to {data['output_file_path']}") 
    except Exception as e:
        print(f"Error: {e}") 

def main():
    parser = argparse.ArgumentParser(description='Generate assessment elements')
    parser.add_argument('-g', '--gui', action='store_true', help='Start the GUI application')
    parser.add_argument('--title', '-t', type=str, help='Assessment Title')
    parser.add_argument('--element-type', '-e', type=str, choices=["Reverse interrogation", "Deduce the question"], default="Reverse interrogation", help='Elements Type')
    parser.add_argument('--number-of-elements', '-n', type=int, default=1, help='Number of Elements')
    parser.add_argument('--output-file-type', '-oft', type=str, choices=["Text", "Word document", "Excel sheet"], default="Text", help='Output File Type')
    parser.add_argument('--output-file-path', '-ofp', type=str, help='Output File Path')
    args = parser.parse_args()

    if args.gui:
        app = Gui()
        app.mainloop()
    else:
        if not args.element_type or not args.number_of_elements:
            parser.error("the following arguments are required: -e/--element-type, -n/--number-of-elements")
        perform_action_cli(args)

