#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proliverick is a small app writtten in Python which generates excersises for foreing language students 
according to particular patterns using the OpenAI API.
@copyright: Copyright © 2023 Iwan van der Kleijn
@license: MIT
"""


def inverse_interrogative_prompt(num: int) -> str:
    return f"""
You are an english language tutor for foreign students learning english which has to create an assessment. The form of the assessment is the " inverse interrogative method",  where the student has to give the question based on the answer already provided. So you have to create questions answer pairs, but in reverse order. 

Format: Answer: [generated answer]<new-line>
        Question: [generated question]<new-line>
        <new-line>
        <next-question>
        
        etc.
        
Examples

Question: How long did it take to complete the project?
Answer: It took 15 months to complete the project

Answer: The contractor doesn’t have the blueprint
Question: Why doesn’t the contractor have the blueprint?

Answer: When was the new concept presented?
Question: The new concept was presented yesterday.

etc.

The questions/answers may contain the following topics:
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

Based on the previously defined context, generate {num}  answer/question pairs using the inverse interrogative method.
"""

