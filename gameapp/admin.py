from django.contrib import admin
from .models import Answer,Question,UserAnswer
# Register your models here.
admin.site.register(Answer)
admin.site.register(UserAnswer)

class AnswerInline(admin.StackedInline):
    model=Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]
    list_display=('question','marks',)