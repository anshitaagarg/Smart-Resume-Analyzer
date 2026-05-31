import streamlit as st
from utils.extract_name import extract_name
from utils.extract_text import extract_text_from_pdf
from utils.extract_contact import extract_email
from utils.extract_contact import extract_phone
from utils.extract_skills import extract_skills

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
    
    st.subheader("Contact Information")
    # Display the extracted email and phone number
    # st.write(f"📧 Email: {email}")
    # st.write(f"📱 Phone: {phone}") w/out coloured boxes around it
    
    st.success(f"👤 Name: {name}")
    st.success(f"📧 Email: {email}")
    st.info(f"📱 Phone: {phone}")
    st.subheader("Detected Skills")

    if skills:
        skill_text = " | ".join(skills)
        st.info(skill_text)
    else:
        st.warning("No skills detected")
         
    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=400
    )