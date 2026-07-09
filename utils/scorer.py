def calculate_ats_score(matched_skills, jd_skills):
    """
    Calculate ATS Match Score.

    Parameters:
        matched_skills (list): Skills present in both resume and job description.
        jd_skills (list): Skills extracted from the job description.

    Returns:
        float: ATS score as a percentage.
    """

    # Avoid division by zero
    if len(jd_skills) == 0:
        return 0.0

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2)