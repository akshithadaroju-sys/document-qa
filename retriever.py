import re


class Retriever:
    def clean(self, text):
        return re.findall(r"\w+", text.lower())

    def retrieve(self, question, sections):
        best_section = ""
        best_score = 0

        q_words = set(self.clean(question))

        for sec in sections:
            sec_words = set(self.clean(sec))
            score = len(q_words.intersection(sec_words))

            if score > best_score:
                best_score = score
                best_section = sec

        return best_section
