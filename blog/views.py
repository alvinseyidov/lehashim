from django.shortcuts import render
from core.models import *
from blog.models import BlogCategory as Category


def category(request, id):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'category.html', context)


def blog(request, id):
    categories = Category.objects.filter(parent__isnull=True)
    category = Category.objects.get(pk=id)
    general = General.objects.all()
    socials = Social.objects.all()
    context = {
        "category": category,
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'blog.html', context)