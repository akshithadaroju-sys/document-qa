def retrieve(question, sections):

    best_section = ""
    best_score = 0

    q_words = set(question.lower().split())

    for sec in sections:

        score = len(
            q_words.intersection(
                set(sec.lower().split())
            )
        )

        if score > best_score:
            best_score = score
            best_section = sec

    return best_section