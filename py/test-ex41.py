def convert():
    results = []
    snippet = ['a', 'b', 'c']
    phrase = ['a1', 'b1', 'c1']
    for sentence in snippet, phrase:
        result = sentence[:]
        results.append(result)


    print "show me the result ", results
    return results


question, answer = convert()
print question
print answer
