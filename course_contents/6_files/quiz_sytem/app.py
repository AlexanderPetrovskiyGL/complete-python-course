with open('questions.txt', 'r') as file:
    questions_with_answers = [question.strip() for question in file.readlines()]

score = 0
total = len(questions_with_answers)

for question_with_answer in questions_with_answers:
    q, a = question_with_answer.split('=')
    ua = input(f'{q}=')
    if ua == a:
        score += 1

with open('result.txt', 'w') as file:
    file.write(f'Your final score is {score}/{total}.')
