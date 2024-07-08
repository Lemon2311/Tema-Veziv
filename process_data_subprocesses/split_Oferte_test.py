import os
from docx import Document

path_Oferte_test = 'Oferte_test'

files = [f for f in os.listdir(path_Oferte_test)]

def get_text_from_docx(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def get_substring_starting_from_phrase(text, phrase):
    position = text.find(phrase)
    if position != -1:
        return text[:position].rstrip()
    else:
        return text.rstrip()
    
def get_substring_starting_from_space(text):
    position = text.find('\n')
    if position != -1:
        return text[position+1:]
    else:
        return text

def split_text():
    for f in files:
        with open(f"input/{os.path.splitext(f)[0] + ".txt"}", 'w', encoding='utf-8') as file:
            file.write(f"{get_substring_starting_from_phrase(get_text_from_docx(f"{path_Oferte_test}/{f}"), "\n")}")

        with open(f"output/{os.path.splitext(f)[0] + ".txt"}", 'w', encoding='utf-8') as file:
            file.write(f"{get_substring_starting_from_space(get_text_from_docx(f"{path_Oferte_test}/{f}"))}")

split_text()