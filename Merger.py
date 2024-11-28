from pypdf import PdfWriter
import os

merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]
# files=os.listdir() 

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf2.pdf")
merger.close()



# python -m venv env
# .env\Scripts\activate
# deactivate
# pip freeze > requirements.txt
# python -m pip install -r requirements.txt
# pip install PyPDF2