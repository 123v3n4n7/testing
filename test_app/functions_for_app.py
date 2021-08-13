from decimal import Decimal
from rest_framework.exceptions import ValidationError

from test_app.models import ListOfQuestion


def get_result_of_testing(test_id, right_answer_dict, answers, incorrect_answers,
                          correct_answers, percent_of_correct_answers):
    try:
        questions = ListOfQuestion.objects.filter(id=test_id)[0].question_set.all()
    except IndexError:
        raise ValidationError(f"Нет теста с id {test_id}!")
    for question in questions:
        right_answer_dict.update({question.id: question.choice_set.filter(is_right=True)[0].id})
    if len(answers) < len(right_answer_dict):
        raise ValidationError("Нужно ответить на все вопросы!")
    for answer in answers:
        question_id = answer['question_id']
        user_answer = answer['сhoice_id']
        try:
            if user_answer != right_answer_dict[question_id]:
                incorrect_answers += 1
            else:
                correct_answers += 1
        except KeyError:
            raise ValidationError(f"Нет вопроса с id {question_id}")
    if correct_answers > 0:
        percent_of_correct_answers = Decimal(correct_answers * 100 / len(right_answer_dict))
        percent_of_correct_answers = percent_of_correct_answers.quantize(Decimal('0.01'))
    elif correct_answers == 0:
        percent_of_correct_answers = 0
    elif correct_answers == len(right_answer_dict):
        percent_of_correct_answers = 100
    result_of_testing = {"correct_answers": correct_answers,
                         "incorrect_answers": incorrect_answers,
                         "percent_of_correct_answers": percent_of_correct_answers}
    return result_of_testing
