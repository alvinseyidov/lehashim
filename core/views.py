from django.shortcuts import render
from core.models import *
from blog.models import BlogCategory as Category, Blog, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    categories = Category.objects.filter(parent__isnull=True)
    featured = Featured.objects.all()
    topics = HotTopics.objects.all()
    general = General.objects.all()
    blogs = Blog.objects.all()
    blogsf = Blog.objects.all()[:3]
    blogsfmobile = Blog.objects.all()[:1]
    tags = Tag.objects.all()[:6]
    socials = Social.objects.all()



    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 2)
    try:
        blgs = paginator.page(page)
    except PageNotAnInteger:
        blgs = paginator.page(1)
    except EmptyPage:
        blgs = paginator.page(paginator.num_pages)

    context = {
        "tags": tags,
        "blogs": blgs,
        "blogsf": blogsf,
        "blogsfmobile": blogsfmobile,
        "topics": topics,
        "general": general,
        "featured": featured,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'index.html', context)


def about(request):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    blogs = Blog.objects.all()[:4]
    topics = HotTopics.objects.all()
    context = {
        "topics": topics,
        "general": general,
        "blogsmost": blogs,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'about.html', context)

def reviews(request):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    blogs = Blog.objects.all()[:4]
    topics = HotTopics.objects.all()
    context = {
        "topics": topics,
        "general": general,
        "blogsmost": blogs,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'reviews.html', context)

def portfolio(request):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    blogs = Blog.objects.all()[:4]
    topics = HotTopics.objects.all()
    context = {
        "topics": topics,
        "general": general,
        "blogsmost": blogs,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'portfolio.html', context)

def contact(request):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    topics = HotTopics.objects.all()
    context = {
        "topics": topics,
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'contact.html', context)