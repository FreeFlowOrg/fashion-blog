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
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY,null=False,default='fashion')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title