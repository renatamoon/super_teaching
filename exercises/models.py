# STANDARD IMPORTS
from django.db import models


class Exercise(models.Model):
    ALTERNATIVE_CHOICES = [
        ('A', 1),
        ('B', 2),
        ('C', 3),
        ('D', 4),
        ('E', 5)
    ]

    question = models.TextField(null=False, blank=False)
    first_alternative = models.TextField(null=False, blank=False)
    second_alternative = models.TextField(null=False, blank=False)
    third_alternative = models.TextField(null=False, blank=False)
    fourth_alternative = models.TextField(null=False, blank=False)
    fifth_alternative = models.TextField(null=False, blank=True)
    answer = models.CharField(max_length=3, null=False, blank=False, choices=ALTERNATIVE_CHOICES)


class Answer(models.Model):
    ANSWER_CHOICES = [
        ('A', 1),
        ('B', 2),
        ('C', 3),
        ('D', 4),
        ('E', 5)
    ]

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercises')
    answer = models.CharField(max_length=3, null=False, blank=False, choices=ANSWER_CHOICES)
    is_answered = models.BooleanField(default=True, null=False, blank=False)
