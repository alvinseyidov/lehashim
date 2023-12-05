from django.shortcuts import render
from core.models import *
from blog.models import BlogCategory as Category, Blog, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from service.models import Service
from training.models import Telim


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

    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
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
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
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
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
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
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
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
    trainings = Telim.objects.all()
    services = Service.objects.all()
    context = {
        "trainings": trainings,
        "services": services,
        "topics": topics,
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'contact.html', context)



def telim(request, id):
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
    return render(request, 'training.html', context)



def telims(request):
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
    return render(request, 'trainings.html', context)