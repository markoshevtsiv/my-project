from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title
