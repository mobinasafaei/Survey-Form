
from django.contrib.auth.models import User

from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    MASTER = 'master'
    STUDENT = 'student'

    CHOICES_ROLL = (
        (MASTER, 'master'),
        (STUDENT, 'student'),
    )
    roll = models.CharField(max_length=255, choices=CHOICES_ROLL,null=True)
   



class Result(models.Model):
    GOOD = 'good'
    AVERAGE = 'average'
    BAD = 'bad'

    CHOICES_QUESTION = (
        (GOOD, 'good'),
        (AVERAGE, 'average'),
        (BAD, 'bad'),
    )
    student_id = models.CharField(max_length=255)
    q1 = models.CharField(max_length=25, choices=CHOICES_QUESTION)
    q2 = models.CharField(max_length=25, choices=CHOICES_QUESTION)
    q3 = models.CharField(max_length=25, choices=CHOICES_QUESTION)
    q4 = models.CharField(max_length=25, choices=CHOICES_QUESTION)
    q5 = models.CharField(max_length=25, choices=CHOICES_QUESTION)
    q6 = models.CharField(max_length=25, choices=CHOICES_QUESTION)
    q7 = models.CharField(max_length=255)

