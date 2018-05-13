from django.db import models

# Create your models here.

class Post(models.Model):

    fashion = 'fashion'
    beauty =  'beauty'
    lifestyle = 'lifestyle'
    travel = 'travel'
    fitness = 'fitness'

    CATEGORY = (
        (fashion, fashion),
        (beauty,  beauty),
        (lifestyle, lifestyle),
        (travel, travel),
        (fitness, fitness),
    )

    post = models.TextField()
    description = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY,null=False,default='fashion')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.FileField(blank=True, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.CharField(max_length=350)
    website = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Like(models.Model):
    ip = models.CharField(max_length=25)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip