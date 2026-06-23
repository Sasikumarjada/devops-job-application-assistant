resume_skills = [
    "linux",
    "aws",
    "docker",
    "kubernetes",
    "terraform",
    "jenkins",
    "git",
    "python"
]

jobs = [
    "DevOps Engineer AWS Docker Kubernetes",
    "Linux System Administrator",
    "Python Developer",
    "AWS Cloud Engineer",
    "Site Reliability Engineer Kubernetes",
    "Data Analyst"
]

for job in jobs:

    score = 0

    for skill in resume_skills:
        if skill.lower() in job.lower():
            score += 1

    match_percentage = (score / len(resume_skills)) * 100

    print(f"{job} -> {match_percentage:.1f}%")