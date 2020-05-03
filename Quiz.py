from Questions import Questions

question_prompts    =   [
    "What color are apples?\n  (a) Red/Green\n  (b) Blue\n  (c) Yellow\n",
    "\nWhat color are oranges?\n  (a) Green\n  (b) Orange\n  (c) Yellow\n",
    "\nWhat color are Lemons?\n  (a) Red\n  (b) blue\n  (c) Yellow\n\n"
]

questions   =   [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "c")
]

def run_test(questions):
    score   =   0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score   =   score + 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " are correct.")

run_test(questions)