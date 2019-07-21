from django.db import models
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    date = models.CharField(max_length=10)
    type_choices = (
        ('General', 'General'),
        ('Advance', 'Advance'),
        ('Professional', 'Professional'),
    )
    type = models.CharField(max_length=200, choices=type_choices)

    def __str__(self):
        return self.title