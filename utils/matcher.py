def compare_skills(resume_skills, jd_skills):
    """
    Compare resume skills with job description skills.

    Returns:
    - matched_skills
    - missing_skills
    - extra_skills
    """

    # Convert to sets for fast comparison
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    # Skills present in both
    matched_skills = sorted(list(resume_set & jd_set))

    # Skills required but missing
    missing_skills = sorted(list(jd_set - resume_set))

    # Skills in resume but not required
    extra_skills = sorted(list(resume_set - jd_set))

    return matched_skills, missing_skills, extra_skills