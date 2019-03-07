from django.db import models

class Author(models.Model):
    firstname = models.CharField(max_length=40, null=False)
    lastname = models.CharField(max_length=40, null=False)
    bio = models.CharField(max_length=200, null=False, blank=True)

class Article(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Comment(models.Model):
    author_name = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=200, null=False)
    article= models.ForeignKey(Article,related_name='comments', on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=20, null=False)
    article= models.ForeignKey(Article, related_name='tags', on_delete=models.CASCADE)
