from django.db import models
from django.urls import reverse




class Book(models.Model):
 title = models.CharField(max_length=200)
 author = models.CharField(max_length=200)
 published_date = models.DateField(null=True, blank=True)
 isbn = models.CharField(max_length=20, blank=True)
 pages = models.PositiveIntegerField(null=True, blank=True)
 cover_url = models.URLField(blank=True)
 summary = models.TextField(blank=True)


created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)


class Meta:
  ordering = ['-created_at']


def __str__(self):
 return f"{self.title} — {self.author}"


def get_absolute_url(self):
 return reverse('books:detail', kwargs={'pk': self.pk})