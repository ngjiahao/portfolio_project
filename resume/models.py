from django.db import models


class Feedback(models.Model):
    choice_tup = (("1", "Not Satisfied"), ("2", "Less Satisfied"), ("3", "Moderate"),
                  ("4", "Satisfied"), ("5", "Awesome"))
    interviewer = models.CharField(max_length=100)
    rating = models.CharField(max_length=100, default='3')
    comments = models.TextField(max_length=5000)

    def __str__(self):
        return self.interviewer
