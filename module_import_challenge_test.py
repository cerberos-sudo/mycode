trivia = {
    "category": "Entertainment: Film",
    "type": "multiple",
    "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
    "correct_answer": "Frankly, my dear, I don't give a damn.",
    "incorrect_answers": [
        "Here's lookin' at you, kid.",
        "Of all the gin joints, in all the towns, in all the world, she walks into mine…",
        "Round up the usual suspects."
    ]
}

question = trivia["question"]
correct_answer = html.unescape(trivia["correct_answer"])
incorrect1 = html.unescape(trivia["incorrect_answers"][0])
incorrect2 = html.unescape(trivia["incorrect_answers"][1])
incorrect3 = html.unescape(trivia["incorrect_answers"][2])

print(question)
print(incorrect1, incorrect2, incorrect3, correct_answer)

user_answer = input("A, B, C, or D? ")

if user_answer.upper() == "D":
    print("Correct!")

