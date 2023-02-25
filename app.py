from pathlib import Path
import streamlit as st
import requests

from PIL import Image
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
data = requests.get('https://raw.githubusercontent.com/hyperplayer7/jsonresume/main/resume.json').json()

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Bryan Chan - Digital CV using Python & Streamlit"
PAGE_ICON = ":wave:"
NAME = data['basics']['name']
DESCRIPTION = data['basics']['summary']
EMAIL = data['basics']['email']
profile_pic = data['basics']['image']
profiles = data['basics']['profiles']
SOCIAL_MEDIA = {profile["network"]: profile["url"] for profile in profiles}

projectsjson = data['projects']
PROJECTS = {project["name"]: project["url"] for project in projectsjson}

SKILLS = data['skills']

OVERVIEW = data['overview']

WORK = data['work']

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello there!")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📬", EMAIL)

# --- SOCIAL LINKS ---

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
for item in OVERVIEW:
  st.write(f"✅ {item}")

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
for skill in SKILLS:
  for keyword in skill['keywords']:
    st.write(f"- {keyword}")

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

for job in WORK:
    st.write("💻", f"**{job['position']} | {job['name']}**")
    st.write(f"{job['startDate']} - {job['endDate']}\n")
    for highlight in job["highlights"]:
        st.write("- > ", highlight)
    st.write("\n")

# --- Projects & Accomplishments ---

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[🏆 {project}]({link})")
