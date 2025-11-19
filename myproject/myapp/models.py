from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birth_date}"

    class Meta:
        ordering = ['last_name', 'first_name', 'birth_date']


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField(default=timezone.now)
    pages = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"



class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

