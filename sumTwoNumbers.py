def  analysis_by_sentence(question,response):
    result = []
    from Phase1 import classify
    from Phase2 import output,sentence_similarity
    category = classify(str(question))[0][0]
    exp_response= output(str(question))[1]
    similarity = sentence_similarity(str(response).split(),str(exp_response).split())
    judgement = "correct" if similarity >= 0.50 else "incorrect"
    result.append(category)
    result.append(exp_response)
    result.append(similarity)
    result.append(judgement)
    return result