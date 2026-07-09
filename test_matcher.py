from utils.matcher import compare_skills

resume = [
    "Python",
    "SQL",
    "Git",
    "TensorFlow"
]

job = [
    "Python",
    "SQL",
    "Docker",
    "AWS"
]

matched, missing, extra = compare_skills(resume, job)

print("Matched Skills :", matched)
print("Missing Skills :", missing)
print("Extra Skills   :", extra)