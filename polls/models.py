from django.db import models


class Question(models.Model):
    body = models.CharField(max_length=150)


class Answer(models.Model):
    body = models.CharField(max_length=150)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
