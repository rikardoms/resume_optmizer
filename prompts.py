def generate_resume_prompt(resume_text: str, job_text: str) -> str:
    return f"""
You are an expert career advisor and resume writer.
Improve the following resume to match the job posting. Highlight relevant skills, rephrase for impact, and organize content clearly.
At the top of the optimized resume, in a scale from 0 to 100, add the score of how much the resume is aligned with the job description. 
---
Resume:
{resume_text}

---
Job Description:
{job_text}

---
Return the optimized resume below:
"""