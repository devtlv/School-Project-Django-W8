from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import *
from django.http import Http404, HttpResponse
from .models import Question
from pprint import pprint

from .forms import AddQuestionForm


def home(request):
    return render(request, 'home.html')


def question(request, id):
    try:
        question = Question.objects.get(id=id)
        return render(request, 'question.html', {'question':question})
    
    except ObjectDoesNotExist:
        return render(request, '404page.html')


def add_question(request):
    
    if request.method == "GET":
        form = AddQuestionForm()
        return render(request, 'addquestion.html', {'form':form})
    
    if request.method == "POST":

        form = AddQuestionForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('questions')
    


def questions(request):  #Controller (VIEW)
    
    #Calling the Model and asking for Data  (The model calls the DB)
    questions = Question.objects.all()

    #Calling the template and asking for html to be built
    html =  render(request, 'questions.html', {'questions':questions})

    return html


def students(request):
    return redirect('comingsoon')


def comingsoon(request):
    return render(request, 'comingsoon.html')

