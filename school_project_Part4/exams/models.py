from django.db import models
from django.contrib.auth.models import User
import datetime

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'

    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    
    school = models.CharField(max_length=30)
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Question(models.Model):
    
    category = models.CharField(max_length=30)
    text = models.CharField(max_length=100, unique=True)
    difficulty = models.IntegerField(null=False)


    def __repr__(self):
        return f"Q{self.id}: {self.text}"

    def __str__(self):
        return f"Q{self.id}: {self.text}"    
    

class Answer(models.Model):
    text = models.CharField(max_length=50)
    points = models.IntegerField(default=5)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="the_answers")

    def __repr__(self):
        return f"A{self.id}: {self.text}"


class Exam(models.Model):
    date = models.DateField(default=datetime.date.today)
    questions = models.ManyToManyField(Question)


