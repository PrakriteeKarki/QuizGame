from django.db import models

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Question(Base):
     question=models.TextField()
     marks=models.IntegerField(default=1)
     def __str__(self):
         return self.question


class Answer(Base):
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="question_answers")
    def __str__(self):
        return self.answer

class UserAnswer(Base):
    useranswer=models.CharField(max_length=100)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="user_answer")