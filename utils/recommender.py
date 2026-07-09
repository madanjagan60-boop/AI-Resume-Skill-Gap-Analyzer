# utils/recommender.py

SKILL_KNOWLEDGE = {

    "python": {
        "difficulty": "Beginner",
        "priority": "Very High",
        "reason": "Python is the primary programming language for AI, Machine Learning, Data Science and Automation."
    },

    "java": {
        "difficulty": "Intermediate",
        "priority": "High",
        "reason": "Java is widely used for backend development, enterprise applications and Android development."
    },

    "c": {
        "difficulty": "Beginner",
        "priority": "Medium",
        "reason": "C builds strong programming fundamentals and is useful for system programming."
    },

    "c++": {
        "difficulty": "Intermediate",
        "priority": "Medium",
        "reason": "C++ is important for competitive programming, game development and high-performance software."
    },

    "sql": {
        "difficulty": "Beginner",
        "priority": "Very High",
        "reason": "SQL is essential for querying and managing databases."
    },

    "aws": {
        "difficulty": "Intermediate",
        "priority": "Very High",
        "reason": "AWS is the most widely used cloud platform for deploying AI and web applications."
    },

    "docker": {
        "difficulty": "Intermediate",
        "priority": "High",
        "reason": "Docker is used to package and deploy machine learning and web applications."
    },

    "kubernetes": {
        "difficulty": "Advanced",
        "priority": "Medium",
        "reason": "Kubernetes manages large-scale containerized applications."
    },

    "tensorflow": {
        "difficulty": "Intermediate",
        "priority": "High",
        "reason": "TensorFlow is one of the leading Deep Learning frameworks."
    },

    "pytorch": {
        "difficulty": "Intermediate",
        "priority": "High",
        "reason": "PyTorch is widely used in AI research and modern deep learning."
    },

    "machine learning": {
        "difficulty": "Intermediate",
        "priority": "Very High",
        "reason": "Machine Learning is one of the most requested AI skills."
    },

    "deep learning": {
        "difficulty": "Advanced",
        "priority": "High",
        "reason": "Deep Learning powers computer vision, NLP and generative AI."
    },

    "communication": {
        "difficulty": "Beginner",
        "priority": "High",
        "reason": "Communication skills are essential for teamwork and interviews."
    },

    "problem solving": {
        "difficulty": "Intermediate",
        "priority": "Very High",
        "reason": "Problem-solving is one of the most valued skills during technical interviews."
    },

    "git": {
        "difficulty": "Beginner",
        "priority": "High",
        "reason": "Git is the standard version control system used by software developers."
    }

}


def recommend_skills(missing_skills):

    recommendations = {}

    for skill in missing_skills:

        key = skill.lower()

        if key in SKILL_KNOWLEDGE:

            recommendations[key] = SKILL_KNOWLEDGE[key]

        else:

            recommendations[key] = {

                "difficulty": "Intermediate",

                "priority": "Medium",

                "reason": f"{skill.title()} is an important industry skill that can improve your employability."

            }

    return recommendations