def calcular_score(estudante, curso):
    score = 0

    # Notas (peso 30%)
    for materia, nota in estudante["notas"].items():
        nota_min = curso["notas_min"].get(materia,0)
        score += min(nota/nota_min,1) * 30

    # Interesses / Skills (peso 30%)
    matching_skills = set(estudante["interesses"]).intersection(set(curso["skills"]))
    score += (len(matching_skills)/len(curso["skills"]))*30

    # Preferência de carreira (peso 20%)
    if estudante["preferencia_trabalho"] in curso["carreira"]:
        score += 20

    # Quiz (peso 20%)
    quiz_score = sum(estudante["quiz"])/ (len(estudante["quiz"])*5) * 20
    score += quiz_score

    return round(score,2)
