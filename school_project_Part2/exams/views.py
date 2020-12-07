from django.shortcuts import render
from django.core.exceptions import *
from .models import Question

def randomq(request):
    pass


def question(request, id):

    try:
        question = Question.objects.get(id=id)
        return render(request, 'question.html', {'question':question})
    
    except ObjectDoesNotExist:
        return render(request, '404page.html')



def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions':questions})