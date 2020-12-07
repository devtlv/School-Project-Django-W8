from django.urls import path
from . import views

urlpatterns = [
  path('', views.randomq, name='randomq'),
  path('question/<int:id>/', views.question, name='question'),
  path('questions/', views.questions, name='questions')
]