from django.contrib import admin
from .models import Question, Choice, ListOfQuestion, Answer

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ListOfQuestion)
admin.site.register(Answer)
