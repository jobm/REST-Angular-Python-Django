from django.db import models

# Create your models here.


class TodoItems(models.Model):
    item = models.CharField(blank=False,max_length=50)
    description = models.CharField(blank=False,max_length=200)
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __init__(self):
       return self.item