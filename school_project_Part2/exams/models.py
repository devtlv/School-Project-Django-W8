from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    difficulty = models.IntegerField()

    def __repr__(self):
        return f"Q{self.id}: {self.text}"
    

    def bark(self):
        print("WOOF")


