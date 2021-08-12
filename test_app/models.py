from django.db import models
from django.contrib.auth.models import User

class ListOfQuestion(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ListOfQuestion"
        verbose_name_plural = "ListOfQuestions"


class Question(models.Model):
    title = models.TextField(blank=False, verbose_name='Текст вопроса')
    list_of_question = models.ForeignKey(ListOfQuestion, on_delete=models.CASCADE, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    title = models.TextField(blank=False, verbose_name='Текст варианта ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    is_right = models.BooleanField(default=False, verbose_name='Верный вариант')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_right is True:
            choices_is_right = self.question.choice_set.filter(is_right=True).first()
            if choices_is_right is not None:
                self.is_right = False
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    test_id = models.ForeignKey(ListOfQuestion, on_delete=models.CASCADE, verbose_name='Тест', default=None)
    result = models.CharField(max_length=100, verbose_name='Результаты', default=None)

    class Meta:
        verbose_name = "Answer of User"
        verbose_name_plural = "Answers of User"
