
import streamlit as st
import os
import google.generativeai as genai
from PyPDF2 import PdfReader

# Google API anahtarınızı burada ayarlayın
genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxx")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_output(pdf_text, job_description, prompt):
    full_prompt = prompt.format(job_description=job_description)
    response = model.generate_content([pdf_text, full_prompt])
    return response.text

def read_pdf(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        pdf_text = ""
        for page_num in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page_num].extract_text()
        return pdf_text
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title='CV AI ANALYZER')
st.header("Get your resume ATS score with feedback")

prompt = """
Objective: Optimize the user's resume to increase its ATS score and enhance their chances of securing a job in the specified domain.

Job Description:
{job_description}

Instructions:

Profession Fit:

Identify the profession or job roles the resume is best suited for.
Strengths:

Highlight the strong points of the resume.
Areas for Improvement:

Identify sections that need enhancement.
Provide specific suggestions for improvements.
Scoring Parameters (Rate each out of 10):

Impact: The effectiveness of the achievements and contributions mentioned.
Brevity: The clarity and conciseness of the content.
Style: The overall presentation and readability.
Sections: The organization and completeness of different resume sections.
Skills: Relevance and prominence of listed skills.
Section Reviews:

Provide a brief review and feedback for each section of the resume (e.g., Summary, Experience, Education, Skills, etc.).
ATS Score:

Assign an ATS score out of 100 based on the resume’s alignment with the job description and its overall quality.
Output:
Ensure the feedback is structured clearly and comprehensively, addressing all points above.
"""

upload_file = st.file_uploader("Upload PDF here", type=["pdf"])
job_description = st.text_area("Enter Job Description here", height=300)

submit_button = st.button("Get ATS Score")

if submit_button:
    if upload_file is not None and job_description:
        pdf_text = read_pdf(upload_file)
        response = get_gemini_output(pdf_text, job_description, prompt)
        st.subheader("Here's the detailed analysis: ")
        st.write(response)
    elif not upload_file:
        st.warning("Please upload a PDF resume.")
    elif not job_description:
        st.warning("Please enter a job description.")
