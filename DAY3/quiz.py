from questions import Question
questions_prompt = [
    "What color are apples?\n a) Red \nb)Blue \nc)Orange\n\n",
    "What color are oranges?\n a) Red \nb)Blue \nc)Orange\n\n",
    "What color are oceans?\n a) Red \nb)Blue \nc)Orange\n\n",
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b")

]

