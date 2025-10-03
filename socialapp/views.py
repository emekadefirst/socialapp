from django.shortcuts import render, redirect
from .models import Post, Comment

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})



def create_post(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        if caption and image:
            Post.objects.create(caption=caption, image=image)
            return redirect("index")
        return render(request, 'create.html', {'error': 'Caption and image are required.'})
    return render(request, 'create.html')

def add_comment(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            post = Post.objects.get(id=post_id)
            comment = Comment.objects.create(post=post, text=text)
            return redirect("index")
        return render(request, 'index.html', {'error': 'comment text is required.'})
    return render(request, 'index.html')