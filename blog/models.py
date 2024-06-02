from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    tittle=models.CharField(max_length=30)
    creat=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    tittle=models.CharField(max_length=75)
    body=models.TextField()
    img=models.ImageField(upload_to='img/articles')
    creat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tittle} - {self.body[:30]}'