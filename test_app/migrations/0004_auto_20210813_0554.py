# Generated by Django 3.2.6 on 2021-08-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20210812_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ пользователя', 'verbose_name_plural': 'Ответы пользователей'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Вариант ответа', 'verbose_name_plural': 'Варианты ответа'},
        ),
        migrations.AlterModelOptions(
            name='listofquestion',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AddField(
            model_name='answer',
            name='num_of_corr_answers',
            field=models.IntegerField(null=True, verbose_name='Количество правильных ответов'),
        ),
        migrations.AddField(
            model_name='answer',
            name='num_of_incorr_answers',
            field=models.IntegerField(null=True, verbose_name='Количество неправильных ответов'),
        ),
        migrations.AddField(
            model_name='answer',
            name='percent_of_corr_answers',
            field=models.DecimalField(decimal_places=2, max_digits=22, null=True, verbose_name='Процент правильных ответов'),
        ),
    ]