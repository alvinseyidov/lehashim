from django.shortcuts import render
from core.models import *
from blog.models import MainCategory


def index(request):
    categories = MainCategory.objects.all()
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'index.html', context)


def about(request):
    categories = MainCategory.objects.all()
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'about.html', context)


def contact(request):
    categories = MainCategory.objects.all()
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'contact.html', context)