from django.forms import ModelForm
from django import forms
from .models import Question, Student


class AddQuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


   
