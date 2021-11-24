from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"current_time": datetime.now(),
                   "posts": Post.objects.all(),
                   "num_posts": Post.objects.count()})