from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField()
    telegram_link = models.CharField(max_length=50, unique=True)


class Question(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    question = models.TextField()
    answer = models.CharField(max_length=200)
    link_to_answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
