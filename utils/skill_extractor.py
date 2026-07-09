import pandas as pd
import re

# Load skill database
skills_df = pd.read_csv("data/processed/technical_skills_database.csv")

# Convert skills to lowercase
skills = skills_df["Skill"].str.lower().tolist()


def extract_skills(text):
    """
    Extract technical skills from resume text.
    """

    text = text.lower()
    text = text.replace("-", " ")
    text = text.replace("/", " ")
    text = text.replace("&", " and ")
    found_skills = []

    for skill in skills:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))