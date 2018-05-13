from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.

def index(request):
    ip = get_client_ip(request)
    return render(request, 'index.html', {})

def fashion(request):
    posts = Post.objects.filter(category="fashion")
    ip = get_client_ip(request)
    likes = Like.objects.filter(ip=ip).values_list('post', flat=True)
    return render(request, 'posts.html', {'posts':posts, 'category':"Fashion", 'href':"fashion", 'likes':likes})

def beauty(request):
    posts = Post.objects.filter(category="beauty")
    ip = get_client_ip(request)
    likes = Like.objects.filter(ip=ip).values_list('post', flat=True)
    return render(request, 'posts.html', {'posts':posts, 'category':"Beauty", 'href':"beauty", 'likes':likes})

def lifestyle(request):
    posts = Post.objects.filter(category="lifestyle")
    ip = get_client_ip(request)
    likes = Like.objects.filter(ip=ip).values_list('post', flat=True)
    return render(request, 'posts.html', {'posts':posts, 'category':"Lifestyle", 'href':"lifestyle", 'likes':likes})

def travel(request):
    posts = Post.objects.filter(category="travel")
    ip = get_client_ip(request)
    likes = Like.objects.filter(ip=ip).values_list('post', flat=True)
    return render(request, 'posts.html', {'posts':posts, 'category':"Travel", 'href':"travel", 'likes':likes})

def fitness(request):
    posts = Post.objects.filter(category="fitness")
    ip = get_client_ip(request)
    likes = Like.objects.filter(ip=ip).values_list('post', flat=True)
    return render(request, 'posts.html', {'posts':posts, 'category':"Fitness", 'href':"fitness", 'likes':likes})

def show_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    ip = get_client_ip(request)
    likes = Like.objects.filter(ip=ip).values_list('post', flat=True)
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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    return ip

def like(request):
    if request.method == "GET":
        pk = request.GET['pk']
        print(pk)
        post = Post.objects.get(pk=pk)
        if 'ip' in request.session:
            ip = request.session['ip']
        if Like.objects.filter(post=post, ip=ip).exists():
            obj = Like.objects.filter(post=post, ip=ip)
            obj.delete()
            post.likes -= 1
            post.save()
        else:
            obj = Like.objects.create(post=post, ip=ip)
            post.likes += 1
            post.save()
    return JsonResponse({ 'likes':post.likes })