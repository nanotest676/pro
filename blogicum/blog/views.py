from django.shortcuts import render
import datetime
from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all().filter(pub_date__lte=datetime.datetime.now(), is_published__exact=True)[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post_detail = Post.objects.values('title', 'location', 'pub_date', 'author', 'text', 'is_published').filter(id__exact=id)
    context = {'post': post_detail}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_category = Category.objects.values('title', 'description').filter(category__exact=category_slug)
    context = {'category': post_category}
    return render(request, template, context)
