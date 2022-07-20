import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
#Setting up models, or database layout. For polling, a question and choice
#Both are subclasses of the class from django.db.Model
#Each has different variables, or table columns: pub_date, choice, votes
#Each field of the database is an instance of Field class from models
#Field is specified what type of data by Char or DateTime etc. 
#foreign key class in line 15 indicates 1-to-1 relationship between question and choice
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text