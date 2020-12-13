from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import *
from django.http import Http404, HttpResponse
from .models import *
from pprint import pprint

from .forms import AddQuestionForm


def home(request):
    return render(request, 'exams/home.html')


def question(request, id):
    try:
        question = Question.objects.get(id=id)
        return render(request, 'exams/question.html', {'question':question})
    
    except ObjectDoesNotExist:
        return render(request, 'exams/404page.html')


def add_question(request):
    
    if request.method == "GET":
        form = AddQuestionForm()
        return render(request, 'exams/addquestion.html', {'form':form})
    
    if request.method == "POST":

        form = AddQuestionForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('questions')
    


def questions(request):  #Controller (VIEW)
    
    #Calling the Model and asking for Data  (The model calls the DB)
    questions = Question.objects.all()

    #Calling the template and asking for html to be built
    html =  render(request, 'exams/questions.html', {'questions':questions})

    return html


def students(request):
    return render(request, 'exams/students.html', {'students':Student.objects.all()})
    
def student(request, id):
    try:
        student = Student.objects.get(id=id)
        return render(request, 'exams/student.html', {'student':student})
    
    except ObjectDoesNotExist:
        return render(request, 'exams/404page.html')


def comingsoon(request):
    return render(request, 'exams/comingsoon.html')


def search(request):
    if request.method == "GET":
        return render(request, 'exams/search.html')

    if request.method == "POST":
        searchquery = request.POST['searchquery']

        questions = Question.objects.filter(text__icontains = searchquery) | Question.objects.filter(category__icontains = searchquery)
        
        return render(request, 'exams/questions.html', {'questions':questions})