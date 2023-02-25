from pathlib import Path
import streamlit as st

from PIL import Image
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "CV.pdf"
# profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Bryan Chan - Digital CV using Python & Streamlit"
PAGE_ICON = ":wave:"
NAME = "Bryan Chan"
DESCRIPTION = """
I am an experienced Ruby on Rails developer with a deep understanding of the language and framework. I have a passion for creating scalable, maintainable, and high-performance web applications while staying up-to-date with the latest technologies and industry trends.
"""
EMAIL = "bryancarlsonchan@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/bryancarlsonchan/",
    "Github": "https://github.com/hyperplayer7",
    "Dev.to": "https://dev.to/hyperplayer7",
    "Hashnode" : "https://shoshin.hashnode.dev/"
}

PROJECTS = {
"🏆 Build A Digital Resume Using Python & Streamlit": "https://github.com/hyperplayer7/cvpython3streamlit",
"🏆 How to Deploy a Node.js App to Render.com for Free": "https://github.com/hyperplayer7/dfdgdfgdfgd"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello there!")



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = "https://lh4.googleusercontent.com/2D9WP_InDxPQg2li0iVSfWt-SsvA2ADxQvbrbG4oBvv18WDnIZiXtM2NLcp3-hDmNpI=w2400"#Image.open(profile_pic)
# url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # st.image(profile_pic, width=230)
    st.image(profile_pic)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📬", EMAIL)

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
✅ Working as a Software Engineer. Using Rails for making web applications and JSON APIs for building SaaS platforms. Following Ruby best practices and methodologies and also using the latest JS technologies available. Following Agile methodologies to maintain robust development.

✅ Managed my own team composed of web developers, graphic designers, and an SEO analyst.

✅ Providing expertise in SaaS development, contributes to the improvement of existing Ruby on Rails application by using Test Driven Development practices and latest Javascript frameworks.

✅ Experience working with a distributed and fully remote team of experienced developers, QA, and supporting teams in a competitive SaaS company. Demonstrated history of working in the computer software industry with a strong history as a Software Engineer skilled in Ruby on Rails, Software Development, Continuous Integration, Scrum, and Object-Oriented Programming (OOP).

"""
)

# --- SKILLS ---

st.write("#")

st.subheader("Hard Skills")

st.write(
"""
- Web Development
- Ruby
- Ruby on Rails
- Mysql
- Postgres
- Git
- Jquery
- HTML
- CSS
- Javascript
- JSON
- API
- Rspec
- Python
- Node.js
"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#--- JOB1
st.write("💻", "**Ruby on Rails Developer | LaunchPad Recruits / Outmatch / Harver**")
st.write("07/2013 - Present")

st.write(
"""
- > Developing and maintaining web applications using the Ruby on Rails framework
- > Designing, coding, and testing software applications
- > Creating and maintaining databases and database structures
- > Developing and implementing software algorithms and data structures
- > Debugging and fixing software defects and issues
- > Collaborating with other developers and designers to deliver high-quality software solutions
- > Participating in code reviews and providing feedback to other developers
- > Staying up-to-date with the latest technologies and trends in web development
- > Providing technical support to end-users and resolving technical issues
- > Planning and executing software development projects
- > Writing clean, efficient, and well-organized code that follows industry best practices
- > Optimizing application performance and scalability
- > Participating in Agile software development methodologies such as Scrum

"""
)

#--- JOB2
st.write("💻", "**Ruby on Rails Developer | Ripplewave**")
st.write("09/2012 - 06/2013")

st.write(
"""
- > Developing and maintaining web applications using the Ruby on Rails framework
- > Designing, coding, and testing software applications
- > Creating and maintaining databases and database structures
- > Developing and implementing software algorithms and data structures
- > Debugging and fixing software defects and issues
- > Collaborating with other developers, designers, and clients to deliver high-quality software solutions
- > Providing technical support to end-users and resolving technical issues
- > Planning and executing software development projects

"""
)

#--- JOB3
st.write("💻", "**Ruby on Rails Developer | Rivereo / Magenic**")
st.write("01/2011 - 11/2012")

st.write(
"""
- > Developing and maintaining web applications using the Ruby on Rails framework
- > Designing, coding, and testing software applications
- > Creating and maintaining databases and database structures
- > Developing and implementing software algorithms and data structures
- > Debugging and fixing software defects and issues
- > Collaborating with other developers, designers, and clients to deliver high-quality software solutions
- > Providing technical support to end-users and resolving technical issues
- > Planning and executing software development projects
- > Participating in Agile software development methodologies such as Scrum

"""
)

#--- JOB4
st.write("💻", "**Ruby on Rails Developer | Brewed Concepts**")
st.write("10/2007 - 01/2011")

st.write(
"""
- > Developing and maintaining web applications using the Ruby on Rails framework
- > Designing, coding, and testing software applications
- > Creating and maintaining databases and database structures
- > Developing and implementing software algorithms and data structures
- > Debugging and fixing software defects and issues
- > Collaborating with other developers, designers, and clients to deliver high-quality software solutions
- > Providing technical support to end-users and resolving technical issues


"""
)

# --- Projects & Accomplishments ---

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
