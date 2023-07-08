#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""
import argparse
from gui import Gui

def perform_action_cli(args):
    data = {'title': args.title, 'element_type': args.element_type, 'number_of_elements': args.number_of_elements}
    print(data)

def main():
    parser = argparse.ArgumentParser(description='Generate assessment elements')
    parser.add_argument('-g', '--gui', action='store_true', help='Start the GUI application')
    parser.add_argument('-t', '--title', type=str, help='Assessment title', default="")
    parser.add_argument('-e', '--element-type', type=str, choices=['Open question', 'Deduce the question'], help='Type of elements')
    parser.add_argument('-n', '--number-of-elements', type=int, choices=range(1, 17), help='Number of elements')
    args = parser.parse_args()

    if args.gui:
        app = Gui()
        app.mainloop()
    else:
        if not args.element_type or not args.number_of_elements:
            parser.error("the following arguments are required: -e/--element-type, -n/--number-of-elements")
        perform_action_cli(args)

if __name__ == "__main__":
    main()
