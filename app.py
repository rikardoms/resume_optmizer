import streamlit as st
from prompts import generate_resume_prompt
from utils import parse_resume, parse_job_posting, call_openai_api, export_to_docx

st.set_page_config(page_title="ResumeGPT", layout="centered")
st.title("ResumeGPT - AI-Powered Resume Optimizer")

uploaded_resume = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
uploaded_job = st.file_uploader("Upload the Job Description", type=["txt", "pdf","docx"])

if uploaded_resume and uploaded_job:
    resume_text = parse_resume(uploaded_resume)
    job_text = parse_job_posting(uploaded_job)

    with st.spinner("Analyzing and rewriting your resume..."):
        prompt = generate_resume_prompt(resume_text, job_text)
        optimized_resume = call_openai_api(prompt)

    st.subheader("Optimized Resume")
    st.text_area("", optimized_resume, height=500)

    st.download_button("Download as Text", optimized_resume, file_name="optimized_resume.txt")
    docx_bytes = export_to_docx(optimized_resume)
    st.download_button("Download as DOCX", docx_bytes, file_name="optimized_resume.docx")