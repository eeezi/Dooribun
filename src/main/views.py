from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
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

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.area = request.POST['area']
        post.location = request.POST['location']
        post.item = request.POST['item']
        post.price = request.POST['price']
        post.head = request.POST['head']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def detail(request, chat_id):
    chat_detail = get_object_or_404(Post, pk=chat_id)
    return render(request, 'detail.html', {'chat_detail':chat_detail})