from django.db import models
from django.contrib.auth.models import User


class ListOfQuestion(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    title = models.TextField(blank=False, verbose_name='Текст вопроса')
    list_of_question = models.ForeignKey(ListOfQuestion, on_delete=models.CASCADE, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    title = models.TextField(blank=False, verbose_name='Текст варианта ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    is_right = models.BooleanField(default=False, verbose_name='Верный вариант')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_right is True:
            self.question.choice_set.filter(is_right=True).update(is_right=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    test_id = models.ForeignKey(ListOfQuestion, on_delete=models.CASCADE, verbose_name='Тест', default=None)
    percent_of_corr_answers = models.DecimalField(max_digits=22, decimal_places=2, null=True,
                                                  verbose_name='Процент правильных ответов')
    num_of_corr_answers = models.IntegerField(null=True, verbose_name='Количество правильных ответов')
    num_of_incorr_answers = models.IntegerField(null=True, verbose_name='Количество неправильных ответов')

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователей"
