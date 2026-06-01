import streamlit as st
import json
from utils.extract_experience import extract_experience
from utils.extract_name import extract_name
from utils.extract_text import extract_text_from_pdf
from utils.extract_contact import extract_email
from utils.extract_contact import extract_phone
from utils.extract_skills import extract_skills
from utils.extract_education import extract_education
from utils.extract_experience import extract_experience
from utils.resume_score import calculate_resume_score

st.title("📄 AI Resume Parser")
st.write("Upload a PDF resume and extract structured information.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)

    email = extract_email(text)
    phone = extract_phone(text)
    name = extract_name(text)
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)

    st.subheader("Contact Information")
    
    st.success(f"👤 Name: {name}")
    st.success(f"📧 Email: {email}")
    st.info(f"📱 Phone: {phone}")
    
    st.subheader("Skills")

    if skills:
        skill_text = " | ".join(skills)
        st.info(skill_text)
    else:
        st.warning("No skills detected")
        
    st.subheader("🎓 Education")

    if education:
        education_block = "\n".join(education)
        st.info(education_block)
    else:
        st.warning("No education information found")
    
    st.subheader("💼 Experience")

    if experience:
        experience_block = "\n".join(experience)
        st.info(experience_block)
    else:
        st.warning("No experience found")
        
    score = calculate_resume_score(
        name,
        email,
        phone,
        skills,
        education,
        experience
    )
    
    parsed_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
        "resume_score": score
    }
    
    json_data = json.dumps(
        parsed_data,
        indent=4
    )
    
    st.subheader("📊 Resume Score")
    
    st.metric(
        label="Overall Score",
        value=f"{score}/100"
    )
    st.progress(score / 100)
         
    show_text = st.checkbox("Show Extracted Resume Text")

    if show_text:
        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            text,
            height=400
        )
    
    st.download_button(
        label="📥 Download Parsed Resume Data",
        data=json_data,
        file_name="parsed_resume.json",
        mime="application/json"
    )
    st.subheader("📄 Parsed JSON Preview")
    st.json(parsed_data)