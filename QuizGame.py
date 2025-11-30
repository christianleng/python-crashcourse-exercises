from typing import List

data_test = [
    {
        "question_text": "What is the capital of France?",
        "answers_question": ["Paris", "London", "Rome"],
        "correct_answers": "a",
    },
    {
        "question_text": "What is the largest planet in our solar system?",
        "answers_question": ["Earth", "Jupiter", "Mars"],
        "correct_answers": "b",
    },
]


def ask_for_answers():
    print("test")


def ask_for_questions(questions: List[dict]):
    countCorrectAnswers = 0

    for question in questions:
        print(question['question_text'])
        for idx, answer in enumerate(question['answers_question']):
            letter = chr(ord("a") + idx)
            print(f"{letter}) {answer}")

        user_answer = input("\nYour answer: ").strip().lower()
        if user_answer == question["correct_answers"]:
            print("Correct!")
            countCorrectAnswers += 1
        else:
            print(
                f"Not correct! The correct answer was {question['correct_answers']}.")

    print(f"\nYour final score: {countCorrectAnswers}/{len(questions)}")


ask_for_questions(data_test)
