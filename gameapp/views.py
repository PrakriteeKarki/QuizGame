from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer,Question,UserAnswer
# Create your views here.
def game(request):
    questions=Question.objects.all().prefetch_related('question_answers')
    score=0
    total=questions.count()
    if request.method=="POST":
       for question in questions:
           selected_option_id = request.POST.get(f"question_{question.id}")
           selected_answer=Answer.objects.get(id=selected_option_id)
           UserAnswer.objects.create(
               useranswer=selected_answer,
               question=question
           )
           if selected_answer.is_correct:
               score+=1
       percentage=(score*100)/total
       return HttpResponse(f"Your Percentage score is {percentage:.2f}%")

    return render(request,'gameapp/home.html',{'questions':questions})