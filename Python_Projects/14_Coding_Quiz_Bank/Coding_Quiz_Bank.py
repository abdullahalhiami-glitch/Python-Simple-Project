import random

questions = [
    {
        "q_id": 1,
        "text": "What is Python?",
        "answer": "Language",
        "category": "Programming",
    }
]


def add_question(q_id, question_text, correct_answer, category):
    if any(q["q_id"] == q_id for q in questions):
        raise ValueError(f"Question with q_id {q_id} already exists.")
    questions.append(
        {
            "q_id": q_id,
            "text": question_text,
            "answer": correct_answer,
            "category": category,
        }
    )


def get_questions_by_category(category):
    return [
        q
        for q in questions
        if q["category"].strip().lower() == str(category).strip().lower()
    ]


def check_answer(q_id, user_answer):
    for q in questions:
        if q["q_id"] == q_id:
            return q["answer"].strip().lower() == str(user_answer).strip().lower()
    raise ValueError(f"Question with q_id {q_id} not found.")


def generate_random_quiz(num_questions):
    count = min(num_questions, len(questions))
    return random.sample(questions, count)


def update_question_text(q_id, new_text):
    for q in questions:
        if q["q_id"] == q_id:
            q["text"] = new_text
            return True
    return False


def get_all_categories():
    return sorted({q["category"] for q in questions})


def delete_question(q_id):
    for index, q in enumerate(questions):
        if q["q_id"] == q_id:
            del questions[index]
            return True
    return False


def get_total_questions_count():
    return len(questions)
