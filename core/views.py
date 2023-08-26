from django.shortcuts import render
from core.models import *
from blog.models import BlogCategory as Category


def index(request):
    categories = Category.objects.filter(parent__isnull=True)
    featured = Featured.objects.all()
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
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
    context = {
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'about.html', context)


def contact(request):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'contact.html', context)