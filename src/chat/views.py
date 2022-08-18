from django.shortcuts import render, get_object_or_404

from main.models import Post

'''
def chat_index(request):
    return render(request, 'chat/chat_index.html', {})
'''

def chat(request, post_id):
    chat_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'chat_detail.html', {'chat_detail':chat_detail})

