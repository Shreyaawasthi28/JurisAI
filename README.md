# JurisAI
### AI-Powered Legal Research Assistant

---

## 📌 About the Project
JurisAI is an AI-powered legal assistance platform designed to simplify and automate
legal research tasks using Natural Language Processing (NLP) and Machine Learning.

The system provides multiple intelligent modules, including:
- Legal Document Analyzer & Summarizer
- Case Law Search Engine
- AI Legal Chatbot

It helps users quickly understand lengthy legal documents, search relevant case laws,
and interact with an AI assistant for legal queries.

---

## 🚀 Features
- Upload and analyze legal documents (PDF, DOCX, TXT, scanned images)
- OCR-based text extraction from scanned legal documents
- NLP preprocessing and Named Entity Recognition (NER)
- Abstractive legal document summarization using T5 Transformer
- Case law search functionality
- AI-powered legal chatbot

---

## 🛠️ Tech Stack
**Frontend:** React.js  
**Backend:** Python, Django  
**AI / NLP:** SpaCy, NLTK, Hugging Face (T5), TextRank  
**OCR:** Tesseract OCR, PIL  
**Tools:** REST APIs, GitHub  

---

## 👩‍💻 My Contribution
I worked primarily on the **Legal Document Analyzer and Summarizer module**, where I:
- Implemented OCR-based text extraction using Tesseract
- Performed text preprocessing using NLP techniques
- Applied Named Entity Recognition using SpaCy
- Integrated the T5 transformer model for abstractive summarization
- Connected AI pipelines with Django backend APIs

---

## 💡 Design Decisions
Paid services such as Google Vision and AWS Textract were avoided.
The project focuses on open-source, cost-effective, and scalable solutions suitable
for academic and real-world usage.

---

## ▶️ How to Run the Project
1. Clone the repository  
   `git clone https://github.com/Shreyaawasthi28/JurisAI.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the Django server  
   `python manage.py runserver`
