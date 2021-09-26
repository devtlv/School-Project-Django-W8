from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import *
from django.http import Http404, HttpResponse
from .models import *
from pprint import pprint
import json
from .forms import AddQuestionForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.csrf import csrf_exempt

from django.views import generic
from time import sleep

class QuestionList(generic.ListView):
    model = Question
    template_name = 'exams/questions.html'
    

class QuestionDetails(generic.DetailView):   
    model = Question
    template_name = 'exams/question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Fetch a single question
        context['heading'] = "This is a great questions" #add a heading
        return context


class StudentList(generic.ListView):
    model = Student
    template_name = "exams/students.html"


def student(request, id):
    try:
        student = Student.objects.get(id=id)
        return render(request, 'exams/student.html', {'student':student})
    
    except ObjectDoesNotExist:
        return render(request, 'exams/404page.html')


def home(request):
    print("GET", request.GET)
    return render(request, 'exams/home.html')


class AddQuestion(generic.View):
    
    def get(self, request):
        form = AddQuestionForm()
        return render(request, 'exams/addquestion.html', {'form':form})
    
    def post(self, request):
        form = AddQuestionForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('questions')


def comingsoon(request):
    return render(request, 'exams/comingsoon.html')


def search(request):
    if request.method == "GET":
        return render(request, 'exams/search.html')

    if request.method == "POST":
        searchquery = request.POST['searchquery']
        print(searchquery)
        questions = Question.objects.filter(text__icontains = searchquery) | Question.objects.filter(category__icontains = searchquery)
        
        return render(request, 'exams/questions.html', {'question_list':questions})




#  VIEW FUNCTIONS THAT RECEIVE ASYNCRONOUS REQUESTS

@csrf_exempt   # This method does not require csrftoken
def asyncdemo(request):
    # sleep(3)  # Pretend we have a slow server
    data = json.loads(request.body)
    print("User is typing...", data['text'])

    data2 = {
        "uppertext": data['text'].upper(),
    }

    return HttpResponse(json.dumps(data2))



# This async method gets its csrf token from the javascript
def asyncadduser(request):
    data = json.loads(request.body)
    print("Data Received.", "Username:", data['text'])
    try:
        user = User.objects.create_user(username=data['text'], password=data['text']) 
        print("Success")
        return HttpResponse(json.dumps({'status':'success', 'message':'User created'}))
    except:
        print("Error")
        return HttpResponse(json.dumps({'status':'error', 'message':'User could not be created'}))