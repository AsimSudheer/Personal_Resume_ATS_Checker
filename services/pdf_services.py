import spacy
from pypdf import PdfReader
from pathlib import Path

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    raw_text =""
    for page in reader.pages:
        raw_text += page.extract_text()
    try:
         nlp = spacy.load("en_core_web_sm")
         doc = nlp(raw_text)
         entities = []
         for ent in doc.ents:
            entities.append({"text": ent.text, "label": ent.label_})

         print("the text have been extracted succesfully ")
         return entities
    except Exception as e:
        return {"error":str(e)}



    