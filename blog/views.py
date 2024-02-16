from django.shortcuts import render
from core.models import *
from blog.models import Category as Category, Blog, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from service.models import Service
from training.models import Telim


def category(request, id):
    categories = Category.objects.filter(parent__isnull=True)
    category = Category.objects.get(pk=id)
    general = General.objects.all()
    socials = Social.objects.all()

    categories = Category.objects.filter(parent__isnull=True)
    featured = Featured.objects.all()
    topics = HotTopics.objects.all()
    general = General.objects.all()
    blogs = Blog.objects.filter(category=category)
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
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
        "category": category,
        "tags": tags,
        "blogs": blgs,
        "blogsmost": blogs,
        "blogsfmobile": blogsfmobile,
        "topics": topics,
        "general": general,
        "featured": featured,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'category.html', context)


def tag(request, slug):
    categories = Category.objects.filter(parent__isnull=True)
    tag = Tag.objects.get(slug=slug)
    general = General.objects.all()
    socials = Social.objects.all()
    topics = HotTopics.objects.all()
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
        "topics": topics,
        "general": general,
        "tag": tag,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'tag.html', context)

def blog(request, id):

    categories = Category.objects.filter(parent__isnull=True)
    featured = Featured.objects.all()
    topics = HotTopics.objects.all()
    general = General.objects.all()
    blog = Blog.objects.get(pk=id)
    blogs = Blog.objects.all()
    blogsf = Blog.objects.all()[:3]
    blogsfmobile = Blog.objects.all()[:1]
    tags = Tag.objects.all()[:6]
    socials = Social.objects.all()
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
        "blog": blog,
        "general": general,
        "socials": socials,
        "categories": categories,
        "tags": tags,
        "blogs": blogs,
        "blogsf": blogsf,
        "blogsfmobile": blogsfmobile,
        "topics": topics,
        "featured": featured,
    }
    return render(request, 'blog.html', context)