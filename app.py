import streamlit as st
st.set_page_config(
    page_title="Smart Resume Analyser",
    page_icon="📄",
    layout="wide"
)

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

st.sidebar.title("📄 Feature Overview")
st.sidebar.markdown(
    """
    Upload a resume PDF to extract:
    
    -👤 Contact Information
    
    -🧠 Skills
    
    -🎓 Education
    
    -💼 Experience
    
    -📊 Resume Score
    """
)

st.title("📄 Smart Resume Analyzer")
st.markdown("""Upload a PDF resume and extract structured information.""")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:
    st.markdown(
        f"<p style='color:#4CAF50;'>✅ Uploaded: {uploaded_file.name}</p>",
        unsafe_allow_html=True
    )

    text = extract_text_from_pdf(uploaded_file)
     
    email = extract_email(text)
    phone = extract_phone(text)
    name = extract_name(text)
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)

    st.subheader("Contact Information")
    
    st.markdown(f"👤 **Name:** {name}")
    st.markdown(f"📧 **Email:** {email}")
    st.markdown(f"📱 **Phone:** {phone}")
    
    st.subheader("🧠 Skills")

    if skills:
        st.markdown(
            f"<p style='color:#7DD3FC; font-size:18px;'>{' | '.join(skills)}</p>",
            unsafe_allow_html=True
        )
    else:
        st.warning("No skills detected")
        
    st.subheader("🎓 Education")

    if education:
        education_block = "<br>".join(education)
        st.markdown(
            f"<p style='color:#7DD3FC; font-size:18px;'>{education_block}</p>",
            unsafe_allow_html=True
        )
    else:
        st.warning("No education information found")
    
    st.subheader("💼 Experience")

    if experience:
        experience_block = "<br>".join(experience)
        st.markdown(
            f"<p style='color:#7DD3FC; font-size:18px;'>{experience_block}</p>",
            unsafe_allow_html=True
        )
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

st.divider()

st.caption(
    "Built using Python, Streamlit and NLP techniques."
)