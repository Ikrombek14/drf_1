from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    audio = models.FileField(upload_to='audios', null=True, blank=True)
    document = models.FileField(upload_to='documents', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.category.name} - {self.author.name}"
