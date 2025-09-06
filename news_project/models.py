from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DT", "Draft"
        Published = "PB", "Published"
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(timezone.now)    
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-published_at",)

    def  __str__(self):
        return self.title    
