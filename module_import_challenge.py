



trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }


question = trivia["question"]

correct_answer = trivia["correct_answer"]

incorrect1 = html.unescape(trivia["incorrect_answers"][0])

incorrect2 = html.unescape(trivia["incorrect_answers"][1])

incorrect3 = html.unescape(trivia["incorrect_answers"][2])

print([question])

print([incorrect1], [incorrect2], [incorrect3], [correct])

user_answer = input("A , B , C or D?")

if user_answer =="D":
    print("correct!")


