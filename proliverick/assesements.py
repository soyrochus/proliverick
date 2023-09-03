#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""
from typing import List
from enum import Enum
from pathlib import Path
import pandas as pd
from docx import Document

class OutputType(Enum):
    TEXT = 'Text'
    WORD = 'Word document'
    EXCEL = 'Excel sheet'

class AssesementCreator:
    
    def get_inverse_interrogative(self) -> List[str]:
        return ""
     
    @staticmethod
    def write_to_file(output_type: OutputType, output_path: Path, data: List[str]):
        match output_type:
            case OutputType.TEXT:
                with output_path.open('w') as f:
                    f.write('\n'.join(data))
            case OutputType.WORD:
                doc = Document()
                for line in data:
                    doc.add_paragraph(line)
                doc.save(output_path)
            case OutputType.EXCEL:
                df = pd.DataFrame(data, columns=["Data"])
                df.to_excel(output_path, index=False)
            case _:
                raise ValueError(f"Unsupported output type: {output_type}")


# Example Usage:

if __name__ == '__main__':
  
    data = ['Question 1', 'Question 2', 'Question 3']
    AssesementCreator.write_to_file(OutputType.TEXT, Path("output.txt"), data)
    AssesementCreator.write_to_file(OutputType.WORD, Path("output.docx"), data)
    AssesementCreator.write_to_file(OutputType.EXCEL, Path("output.xlsx"), data)
    