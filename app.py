import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.preprocessing import preprocess_text
from utils.skill_extractor import extract_skills
from utils.jd_parser import extract_jd_text
from utils.matcher import compare_skills
from utils.scorer import calculate_ats_score
from utils.recommender import recommend_skills



# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Skill Gap Analyzer",
    page_icon="📄",
    layout="wide"
)



# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.image("assets/logo.png", width=250)

    st.title("AI Resume Analyzer")

    st.markdown("---")

    st.subheader("Project Features")

    st.write("✅ Resume Upload")
    st.write("✅ Resume Parsing")
    st.write("✅ Skill Extraction")
    st.write("✅ ATS Score")
    st.write("✅ Skill Gap Analysis")
    st.write("✅ Skill Recommendations")

    st.markdown("---")

    st.info(
        "B.Tech AI & DS Major Project\n\n"
        "Built using Python + Streamlit"
    )

# -------------------------------------------------------
# Main Title
# -------------------------------------------------------

st.title("📄 AI Resume Skill Gap Analyzer")

st.write(
    "Upload your Resume and compare it with any Job Description."
)

# -------------------------------------------------------
# Upload Resume
# -------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -------------------------------------------------------
# Job Description
# -------------------------------------------------------

job_description = st.text_area(
    "Paste Job Description",
    height=220
)

# -------------------------------------------------------
# Start Processing
# -------------------------------------------------------

if uploaded_file is not None:

    pdf_path = f"uploads/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Resume Uploaded Successfully")

    # ---------------------------------------------------
    # Resume Processing
    # ---------------------------------------------------

    extracted_text = extract_text_from_pdf(pdf_path)

    cleaned_text = preprocess_text(extracted_text)

    resume_skills = extract_skills(cleaned_text)

    # ---------------------------------------------------
    # Resume Information
    # ---------------------------------------------------

    st.header("📄 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Resume Skills",
            len(resume_skills)
        )

    with col2:
        st.metric(
            "Resume Words",
            len(cleaned_text.split())
        )

    # ---------------------------------------------------
    # Resume Skills
    # ---------------------------------------------------

    st.subheader("🛠 Resume Skills")

    if resume_skills:

        st.success(f"{len(resume_skills)} Skills Detected")

        st.write(", ".join(skill.title() for skill in resume_skills))

    else:

        st.warning("No skills detected.")

    # ---------------------------------------------------
    # Resume Text
    # ---------------------------------------------------

    with st.expander("📄 View Extracted Resume Text"):

        st.text_area(
            "",
            extracted_text,
            height=250
        )

    with st.expander("🧹 View Cleaned Resume Text"):

        st.text_area(
            "",
            cleaned_text,
            height=250
        )

    # ---------------------------------------------------
    # Job Description Processing
    # ---------------------------------------------------

    if job_description.strip():

        jd_text = extract_jd_text(job_description)

        jd_clean = preprocess_text(jd_text)

        jd_skills = extract_skills(jd_clean)

        # ---------------------------------------------------
        # Job Description Skills
        # ---------------------------------------------------

        st.header("💼 Job Description Analysis")

        st.metric(
            "JD Skills",
            len(jd_skills)
        )

        st.subheader("📌 Required Skills")

        if jd_skills:

            st.write(", ".join(skill.title() for skill in jd_skills))

        else:

            st.warning("No Job Description skills detected.")

        # ---------------------------------------------------
        # Compare Skills
        # ---------------------------------------------------

        matched_skills, missing_skills, extra_skills = compare_skills(
            resume_skills,
            jd_skills
        )

        # ---------------------------------------------------
        # Skill Recommendations
        # ---------------------------------------------------

        recommendations = recommend_skills(missing_skills)

        # ---------------------------------------------------
        # ATS Score
        # ---------------------------------------------------

        ats_score = calculate_ats_score(
            matched_skills,
            jd_skills
        )

        # ---------------------------------------------------
        # ATS Score Display
        # ---------------------------------------------------

        st.header("📊 ATS Match Score")

        st.progress(ats_score / 100)

        st.success(f"ATS Match Score : {ats_score}%")

        # ---------------------------------------------------
        # Statistics
        # ---------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with col2:
            st.metric(
                "Missing Skills",
                len(missing_skills)
            )

        with col3:
            st.metric(
                "Extra Skills",
                len(extra_skills)
            )

        # ---------------------------------------------------
        # Matching Skills
        # ---------------------------------------------------

        with st.expander("✅ Matching Skills", expanded=True):

            if matched_skills:

                for skill in matched_skills:
                    st.markdown(f"✅ {skill.title()}")

            else:

                st.info("No matching skills found.")

        # ---------------------------------------------------
        # Missing Skills
        # ---------------------------------------------------

        with st.expander("❌ Missing Skills", expanded=True):

            if missing_skills:

                for skill in missing_skills:
                    st.markdown(f"❌ {skill.title()}")

            else:

                st.success("No missing skills.")

        # ---------------------------------------------------
        # Extra Skills
        # ---------------------------------------------------

        with st.expander("⭐ Extra Skills", expanded=True):

            if extra_skills:

                for skill in extra_skills:
                    st.markdown(f"⭐ {skill.title()}")

            else:

                st.info("No extra skills.")

        # ---------------------------------------------------
        # Skill Gap Recommendations
        # ---------------------------------------------------

        with st.expander("📚 Skill Gap Recommendations", expanded=True):

            if recommendations:

                for skill, info in recommendations.items():

                    st.markdown(f"### 🎯 {skill.title()}")

                    st.write(f"**Difficulty:** {info['difficulty']}")

                    st.write(f"**Priority:** {info['priority']}")

                    st.write("**Why should you learn this?**")

                    st.info(info["reason"])

                    st.divider()

            else:

                st.success(
                    "🎉 Congratulations! Your resume matches the Job Description."
                )

    else:

        st.info("👆 Paste a Job Description to calculate ATS Score.")