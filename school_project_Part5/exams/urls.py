from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('questions/', views.questions, name='questions'),
  path('question/<int:id>/', views.question, name='question'),
  path('questions/add/', views.add_question, name='add-question'),
  path('students/', views.students, name='students'),
  path('student/<int:id>', views.student, name='student'),
  path('comingsoon/', views.comingsoon, name='comingsoon'),
  path('search/', views.search, name='search'),
]