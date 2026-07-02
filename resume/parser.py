import re
import spacy
import pdfplumber
from docx import Document
import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')
# Read the PDF file
def read_pdf_file(resume):
    text = ""
    with pdfplumber.open(resume) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Read the DOCX file
def read_docx_file(resume):
    doc = Document(resume)
    text = ''
    for para in doc.paragraphs:
        text+=para.text
    return text

# Extract text from the resume
def extract_text_from_resume(resume):
    if resume.name.endswith('.pdf'):
        return read_pdf_file(resume)
    elif resume.name.endswith('.docx'):
        return read_docx_file(resume)
    return None

# Extract the full name from the text
def extract_full_name(text):
    # Create the Doc object
    doc = nlp(text)

    # Loop through doc.ents to find one labelled PERSON and return its text
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    
    return None

# Extract the email from the text
def extract_email(text):
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if email:
        return email.group(0)
    return None

# Extract the mobile number from the text
def extract_mobile_number(text):
    mobile_number = re.search(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)
    if mobile_number:
        return mobile_number.group(0)
    return None

# Extract the required resume data
def extract_resume_data(resume):
    text = extract_text_from_resume(resume)
    full_name = extract_full_name(text)
    email = extract_email(text)
    mobile_number = extract_mobile_number(text)
    return full_name, email, mobile_number
