from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

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

def show_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'full_post.html', {'post':post, 'comments':comments})

def comment(request, pk):
    post = Post.objects.get(pk=pk)
    name = request.POST['name']
    email = request.POST['email']
    website = request.POST['website']
    comment = request.POST['comment']
    c = Comment.objects.create(post=post, name=name, comment=comment, email=email, website=website)
    c.save()
    return HttpResponseRedirect(reverse('fashion:show_post', args=pk))