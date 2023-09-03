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
from simpleaichat import AIChat
from dotenv import load_dotenv
        
class OutputType(Enum):
    TEXT = 'Text'
    WORD = 'Word document'
    EXCEL = 'Excel sheet'

class AssesementCreator:
    
    def __init__(self):
        load_dotenv()
        self.ai = AIChat( model="gpt-4", console= False, system='You are a system which generated questions for foreign languages students' )

    def get_inverse_interrogative(self) -> List[str]:
        prompt  ="""
Inverse Interrogative generation of questions is the methology  where the student creates the question based on the answer already provided

Examples

Teacher: It took 15 months to complete the project / Student: How long did it take to complete the project?
Teacher: The contractor doesn’t have the blueprint / Student: Why doesn’t the contractor have the blueprint?
Teacher: The new concept was presented yesterday. / Student: When was the new concept presented?

Please create 10 questions with corresponding using the inverse interrogative method.

Format: Question / Answer

        """
        return self.ai(prompt)    
     
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
   
    creator = AssesementCreator()
    data = creator.get_inverse_interrogative()
    print(data)
    

    # AssesementCreator.write_to_file(OutputType.TEXT, Path("output.txt"), data)
    # AssesementCreator.write_to_file(OutputType.WORD, Path("output.docx"), data)
    # AssesementCreator.write_to_file(OutputType.EXCEL, Path("output.xlsx"), data)
    