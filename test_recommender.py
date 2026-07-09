from utils.recommender import recommend_skills

missing = ["aws", "docker", "kubernetes"]

recommendations = recommend_skills(missing)

for skill, info in recommendations.items():
    print(f"\nSkill: {skill.title()}")
    print(f"Difficulty : {info['difficulty']}")
    print(f"Priority   : {info['priority']}")
    print(f"Reason     : {info['reason']}")