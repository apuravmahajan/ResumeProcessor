import re
import spacy
import pdfplumber
from docx import Document
from spacy.matcher import Matcher

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

# Extract the first name from the text
def extract_first_name(text):
    # Load the spacy model
    nlp = spacy.load('en_core_web_sm')

    # Initialize the matcher
    matcher = Matcher(nlp.vocab)

    # Define the patterns
    patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}], 
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}], 
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}] 
    ]

    # Add the patterns to the matcher
    for pattern in patterns:
        matcher.add('NAME', patterns=[pattern])

    # Create a Doc object
    doc = nlp(text)
    #  Apply the matcher to the doc
    matches = matcher(doc)

    # Return the first name from first match if available
    for match_id, start, end in matches:
        span = doc[start:end]
        first_name = span[0]
        return first_name.text

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
    first_name = extract_first_name(text)
    email = extract_email(text)
    mobile_number = extract_mobile_number(text)
    return first_name, email, mobile_number