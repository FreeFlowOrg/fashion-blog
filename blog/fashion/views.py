from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def fashion(request):
    posts = Post.objects.filter(category="fashion")
    return render(request, 'posts.html', {'posts':posts, 'category':"Fashion", 'href':"fashion"})

def beauty(request):
    posts = Post.objects.filter(category="beauty")
    return render(request, 'posts.html', {'posts':posts, 'category':"Beauty", 'href':"beauty"})

def lifestyle(request):
    posts = Post.objects.filter(category="lifestyle")
    return render(request, 'posts.html', {'posts':posts, 'category':"Lifestyle", 'href':"lifestyle"})

def travel(request):
    posts = Post.objects.filter(category="travel")
    return render(request, 'posts.html', {'posts':posts, 'category':"Travel", 'href':"travel"})

def fitness(request):
    posts = Post.objects.filter(category="fitness")
    return render(request, 'posts.html', {'posts':posts, 'category':"Fitness", 'href':"fitness"})
