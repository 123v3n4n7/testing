from decimal import Decimal
from rest_framework.exceptions import ValidationError


def get_result_of_testing(answers, test):
    correct_answers = 0
    incorrect_answers = 0
    percent_of_correct_answers = 0
    right_answer_dict = {}
    for question in test.question_set.all():
        right_answer_dict.update({question.id: question.choice_set.filter(is_right=True)[0].id})
    if len(answers) < len(right_answer_dict):
        raise ValidationError("Нужно ответить на все вопросы!")
    for answer in answers:
        if type(answer) is not dict:
            raise ValidationError('answer должен быть словарём в виде:'
                                  '{"question_id": id-вопроса,'
                                  ' "сhoice_id": id-ответа}')
        try:
            question_id = answer['question_id']
            user_answer = answer['сhoice_id']
        except KeyError:
            raise ValidationError(f"В ответе нет id вопроса или id варианта ответа")
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
