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
from proliverick.console_tools import spinner
from proliverick.gui import Gui

VERSION_LABEL = "0.1.0"


def default_string(value, default=""):
    '''Return the value if it is not Falsy, otherwise return the default'''
    return value if value else default
    
def perform_action_cli(args):
    
    data = {'title': default_string(args.title), 'element-type': args.element_type, 'number-of-elements': args.number_of_elements, 
            'output-file-type': default_string(args.output_file_type, 'Text'), 'output-file-path': default_string(args.output_file_path, 'output.txt')}
    try:
        with spinner("Create assement (contacting AI)..."):
            create_assesement(data)
            
        print(f"File written to {data['output-file-path']}") 
    except Exception as e:
        print(f"Error: {e}") 

def main():
    parser = argparse.ArgumentParser(description='Proliverick - generate assessment elements')
    
    parser.add_argument('-g', '--gui', action='store_true', help='Start the GUI application')
    parser.add_argument('-c', '--commandline', action='store_true', help='Use Command Line interface')
    parser.add_argument('-v', '--version', action='version', version=VERSION_LABEL)

    parser.add_argument('--title', '-t', type=str, help='Assessment Title')
    parser.add_argument('--element-type', '-e', type=str, choices=["Reverse interrogation", "Deduce the question"], default="Reverse interrogation", help='Elements Type')
    parser.add_argument('--number-of-elements', '-n', type=int, default=1, help='Number of Elements')
    parser.add_argument('--output-file-type', '-oft', type=str, choices=["Text", "Word document", "Excel sheet"], default="Text", help='Output File Type')
    parser.add_argument('--output-file-path', '-ofp', type=str, help='Output File Path', default="assesement.txt")
    
    args = parser.parse_args()

    gui = args.gui
    if not gui and not args.commandline:
        gui = True
        
    if gui:
        app = Gui()
        app.mainloop()
    else:
        if not args.element_type or not args.number_of_elements:
            
            parser.error("the following arguments are required: -e/--element-type, -n/--number-of-elements")
        perform_action_cli(args)

