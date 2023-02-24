from pathlib import Path
import streamlit as st

from PIL import Image
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV"
PAGE_ICON = ":wave:"
NAME = "John Doe"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "johndoe@email.com"
SOCIAL_MEDIA = {
    "Youtube" : "",
    "LinkedIn": "https://linkedin.com",
    "Github": "",
    "Twitter": ""
}

PROJECTS = {
"Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb@A9i6d320",
"Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
"Desktop Application - Excel2Csv converter with user settings & menubar": "https://youtu.be/LzCfNanQ"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello there!")



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjx-by4e5r6kDq59HyeRElGTd00oMFr-duASxN8UKnsQ&s"#Image.open(profile_pic)
url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.download_button(
    #     label=" Download Resume",
    #     data=PDFbyte,
    #     file_name = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    #     mime = "application/octet-stream"
    # )
    st.markdown(f"[Download Resume]({url})")
    st.write("@", EMAIL)

# --- SOCIAL LINKS ---

st.write("#")

cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index] .write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---

st.write("#")

st.subheader("Experience & Qulifications")

st.write(
"""
- 7 Years expereince extracting actionable insights from data
- Strong hands on experience and knowledge in Python and Excel
- Good understanding of statistical principles and their respective applications
- Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---

st.write("#")

st.subheader("Hard Skills")

st.write(
"""
- Programming: Python (Scikit-learn, Pandas), SQL, VBA
- Data Visulization: PowerBi, MS Excel, Plotly
- Modeling: Logistic regression, linear regression, decition trees
"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#--- JOB1
st.write("X", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")

st.write(
"""
- > Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives,
and supplied recommendations to boost landing page conversion rate by 38%
- > Lorem Ipsum
- > Lorem Ipsum
"""
)

#--- JOB1
st.write("X", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")

st.write(
"""
- > Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives,
and supplied recommendations to boost landing page conversion rate by 38%
- > Lorem Ipsum
- > Lorem Ipsum
"""
)

#--- JOB1
st.write("X", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")

st.write(
"""
- > Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives,
and supplied recommendations to boost landing page conversion rate by 38%
- > Lorem Ipsum
- > Lorem Ipsum
"""
)

# --- Projects & Accomplishments ---

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

#Reference: https://www.youtube.com/watch?v=BXAeMICmUSQ
#Reference: https://www.youtube.com/watch?v=4SO3CUWPYf0
