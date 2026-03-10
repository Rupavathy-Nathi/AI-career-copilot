def match_jobs(skills):

    jobs = {
        "Backend Developer": ["python","fastapi","docker","mongodb"],
        "Data Analyst": ["python","sql","pandas","excel"],
        "ML Engineer": ["python","tensorflow","pytorch","ml"]
    }

    results = []

    for job, req in jobs.items():

        match = len(set(skills) & set(req))

        score = int((match / len(req)) * 100)

        results.append({
            "role": job,
            "match": score
        })

    return sorted(results, key=lambda x: x["match"], reverse=True)
