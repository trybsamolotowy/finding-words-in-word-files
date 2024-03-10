import docx2txt
import re

text = docx2txt.process("publikacje.docx")

with open("wyodrebnione_publikacje.txt", "w") as output_file:
    lines = text.split("\n")
    for line in lines:
        if re.search(r'\b(child|children|kids|kid|pediatrics)\b', line):
            output_file.write(line + "\n")
