from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone
class Question(models.Model):
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
#    def __init__(self, question_text, pub_date):
#        self.question_text = question_text
#        self.pub_date = pub_date
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
#    def __init__(self, choice_text, votes, question):
#        self.choice_text = choice_text
#        self.votes = votes
#        self.question = question

