from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('questions/', views.QuestionList.as_view(), name='questions'),
  path('question/<int:pk>/', views.QuestionDetails.as_view(), name='question'),
  path('questions/add/', views.AddQuestion.as_view(), name='add-question'),
  path('students/', views.StudentList.as_view(), name='students'),
  path('student/<int:id>', views.student, name='student'),
  path('comingsoon/', views.comingsoon, name='comingsoon'),
  path('search/', views.search, name='search'),
  path('asyncdemo/', views.asyncdemo, name="asyncdemo"),
  path('asyncadduser/', views.asyncadduser, name="asyncadduser")
]