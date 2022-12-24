from questions import questions

import random

score = 0

random.shuffle(questions)

wrongAnswers = []
for question in questions:
    print("-----------------")
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i + 1}: {choice}")
    answer = input("Enter your choice (number): ")
    if answer == question["correct"]:
        score += 1
        print("Correct!")
        print("Explanation: " + question["explanation"] + "\n")
    else:
        wrongAnswers.append(question["question"])
        print("Incorrect.\n")

print("-----------------")
print(f"You scored {score} out of {len(questions)}.\n")
#print("You had problems with the following questions:")
for wrongAnswer in wrongAnswers:
    print("-----------------")
    print(wrongAnswer)
    input("# Press Enter to continue to next wrong question:")