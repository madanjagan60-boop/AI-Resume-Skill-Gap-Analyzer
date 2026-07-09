from utils.scorer import calculate_ats_score

matched = [
    "python",
    "sql",
    "git"
]

jd = [
    "python",
    "sql",
    "docker",
    "aws",
    "git"
]

score = calculate_ats_score(matched, jd)

print("ATS Score:", score, "%")