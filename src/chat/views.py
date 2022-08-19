from django.shortcuts import render, get_object_or_404

from main.models import Post

'''
def room(request):
    return render(request, 'room.html', {})
'''

def chat(request, post_id):
    openchat = get_object_or_404(Post, pk=post_id)
    return render(request, 'openchat.html', {'openchat':openchat})


