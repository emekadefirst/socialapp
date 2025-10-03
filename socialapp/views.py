from django.shortcuts import render, redirect
from .models import Post

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