from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    # posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})
