from questions import questions

import random

score = 0

random.shuffle(questions)

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
        print("Incorrect.\n")

print("-----------------")
print(f"You scored {score} out of {len(questions)}.")