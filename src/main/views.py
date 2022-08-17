from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.location = request.POST['location']
        post.item = request.POST['item']
        post.price = request.POST['price']
        post.head = request.POST['head']
        post.date = timezone.now()
        post.save()
    return redirect('home')
