#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""

# Import necessary modules
import os
import re
from prompt_toolkit.patch_stdout import patch_stdout
import threading
import time
from contextlib import contextmanager


@contextmanager
def spinner(prompt=""):
    def spin():
        if prompt:
            print(prompt)
            
        chars = "|/-\\"
        with patch_stdout():
            while not spinner_stop:
                for char in chars:
                    print('\r' + char, end='', flush=True)
                    time.sleep(0.1)
            print('\r ', end='', flush=True)

    spinner_stop = False
    spinner_thread = threading.Thread(target=spin)
    spinner_thread.start()
    
    try:
        yield
    finally:
        spinner_stop = True
        spinner_thread.join()