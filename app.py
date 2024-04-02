from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_setup(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Input prompts
input_prompt1 = """
As an experienced Technical Human Resource Manager, your responsibility is to assess the suitability of the provided resume for the specified job description. 
Please provide your expert evaluation on whether the candidate's profile aligns with the role. 
Identify and discuss the candidate's strengths and weaknesses in relation to the job requirements.
Resume Content:
{text}
Job Description:
{input_text}
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a profound understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Provide the percentage match of the resume with the job description, followed by the list of missing keywords, if any, and your final thoughts.
Resume Content:
{text}
Job Description:
{input_text}
"""
input_prompt4 ="""
You are tasked with providing a concise overall assessment of the resume's quality and suitability for the job.
Analyze the resume content and provide a brief summary of its strengths, weaknesses, and overall suitability for the specified job description.
Resume Content:
{text}
Job Description:
{input_text}
"""

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description:", key="input")

min_confidence = st.slider("Minimum Confidence", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
use_keywords = st.checkbox("Use Keywords Analysis")

with st.sidebar:
    st.title("Menu:")
    uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])
    if uploaded_file is not None:
        st.success("Done")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")
submit4 = st.button("Assess Overall Resume Quality")

if submit1:
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1.format(text=pdf_content, input_text=input_text))
        st.subheader("Evaluation of the Resume")
        st.write(response)
        st.session_state['uploaded_file'] = None
    else:
        st.write("Please upload the resume and provide the job description.")

if submit3:
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3.format(text=pdf_content, input_text=input_text))
        st.subheader("Matching Percentage and Analysis")
        st.write(response)
        st.session_state['uploaded_file'] = None
    else:
        st.write("Please upload the resume and provide the job description.")

if submit4:
    if uploaded_file is not None and input_text:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4.format(text=pdf_content, input_text=input_text))
        st.subheader("Overall Resume Quality Assessment")
        st.write(response)
        st.session_state['uploaded_file'] = None
    else:
        st.write("Please upload the resume and provide the job description.")
