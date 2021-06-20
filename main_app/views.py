from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from  blog.models import Post
from django.db.models import Count

def index(request):
    latest_blog = Post.objects.order_by("-date_posted")[0:3]
    popular_blog = Post.objects.annotate(like_count=Count('likes')) \
                                 .order_by('-like_count')[0:3]

    context = {
        'latest_blog': latest_blog,
        'popular_blog': popular_blog,
    }
    return render(request, 'main_app/index.html', context)


def base(request):
    return render(request, 'main_app/base.html', {'title': 'about'})