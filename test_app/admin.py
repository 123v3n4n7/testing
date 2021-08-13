from django.contrib import admin
from .models import Question, Choice, ListOfQuestion, Answer


class QuestionsInLine(admin.TabularInline):
    model = Question
    extra = 0


class ChoicesInline(admin.TabularInline):
    model = Choice
    extra = 0


@admin.register(Choice)
class Choice(admin.ModelAdmin):
    list_filter = ['question']
    search_fields = ['question__title']
    list_display = ('title', 'question', 'is_right', 'id',)


@admin.register(ListOfQuestion)
class ListOfQuestion(admin.ModelAdmin):
    list_display = ('title', 'id',)
    inlines = [QuestionsInLine]


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('title', 'list_of_question', 'id',)
    list_filter = ['list_of_question']
    search_fields = ['list_of_question__title']
    inlines = [ChoicesInline]


@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_filter = ['user']
    search_fields = ['user']
    list_display = ('user', 'test_id', 'percent_of_corr_answers', 'num_of_corr_answers', 'num_of_incorr_answers', 'id',)
