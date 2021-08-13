from django.contrib import admin
from .models import Question, Choice, ListOfQuestion, Answer

admin.site.register(Choice)
#admin.site.register(Answer)


class QuestionsInLine(admin.TabularInline):
    model = Question


class ChoicesInline(admin.TabularInline):
    model = Choice


@admin.register(ListOfQuestion)
class ListOfQuestion(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [QuestionsInLine]


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ChoicesInline]


@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display = ('id', 'user', 'test_id', 'percent_of_corr_answers', 'num_of_corr_answers', 'num_of_incorr_answers')
