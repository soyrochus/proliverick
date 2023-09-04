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

Format: Question: {generated question}<new-line>
        Answer: {generated answer}<new-line>
        <new-line>
        <next-question>
        
        etc.
        
Examples

Question: How long did it take to complete the project?
Answer: It took 15 months to complete the project

Question: Why doesn’t the contractor have the blueprint?
Answer: The contractor doesn’t have the blueprint

Question: The new concept was presented yesterday.
Answer: When was the new concept presented?

The topics may contain the following:
- Daily situations
- Work
- History
- Geography
- Science
- Technology
- Art
- Culture
- Sports
- Politics  (non polemical)
- Economy
- Society
- Environment
- Health
- Education
- Religion
- Philosophy
- Psychology
- Law
- Language
- Literature
- Music
- Cinema
- Television
- Media

Generate 10 questions with answers using the inverse interrogative method.

        """
        return self.ai(prompt)    
     
    @staticmethod
    def write_to_file(output_type: OutputType, output_path: Path, data: str):
        
        data_list = data.split('\n')
        match output_type:
            case OutputType.TEXT:
                with output_path.open('w') as f:
                    f.write(data)
            case OutputType.WORD:
                doc = Document()
                for line in data_list:
                    doc.add_paragraph(line)
                doc.save(output_path)
            case OutputType.EXCEL:
                df = pd.DataFrame(data_list, columns=["Data"])
                df.to_excel(output_path, index=False)
            case _:
                raise ValueError(f"Unsupported output type: {output_type}")


def create_assesement(data: dict):
    creator = AssesementCreator()
    if data['element-type'] == "Open question":
        data = creator.get_inverse_interrogative()
        creator.write_to_file(data['output-file-type'], Path(data['output-file-path']), data)
    else:
        raise ValueError(f"Unsupported element type: {data['element-type']}")
    AssesementCreator.write_to_file(data['output-file-type'], Path(data['output-file-path']), data)
# Example Usage:

if __name__ == '__main__':
    pass
    # creator = AssesementCreator()
    # data = creator.get_inverse_interrogative()
    # print(data)
    

    # AssesementCreator.write_to_file(OutputType.TEXT, Path("output.txt"), data)
    # AssesementCreator.write_to_file(OutputType.WORD, Path("output.docx"), data)
    
    # data = """Question: What language is predominantly spoken in Brazil?
    # Answer: Portuguese is predominantly spoken in Brazil.

    # Question: Who is the author of the novel "Pride and Prejudice"?
    # Answer: The author of "Pride and Prejudice" is Jane Austen.

    # Question: What is the capital of Australia?
    # Answer: The capital of Australia is Canberra.

    # Question: Who won the FIFA World Cup in 2018?
    # Answer: France won the FIFA World Cup in 2018.

    # Question: What is the primary function of the heart in the human body?
    # Answer: The primary function of the heart is to pump blood throughout the body.

    # Question: When was the internet invented?
    # Answer: The internet was invented in 1969.

    # Question: Who painted the Mona Lisa?
    # Answer: Leonardo da Vinci painted the Mona Lisa.

    # Question: What is the largest planet in our solar system?
    # Answer: Jupiter is the largest planet in our solar system.

    # Question: Who is the current president of the United States?
    # Answer: The current president of the United States is Joe Biden.

    # Question: What is the main religion practiced in India?
    # Answer: Hinduism is the main religion practiced in India."""

    #     AssesementCreator.write_to_file(OutputType.TEXT, Path("output.txt"), data)
    #     AssesementCreator.write_to_file(OutputType.WORD, Path("output.docx"), data)
    #     AssesementCreator.write_to_file(OutputType.EXCEL, Path("output.xlsx"), data)
    
