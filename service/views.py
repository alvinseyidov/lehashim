from django.shortcuts import render

from core.models import *
from blog.models import Category as Category, Blog, Tag
from event.models import Event

from service.models import Service
from training.models import Telim

def service(request, id):
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    blogs = Blog.objects.all()[:4]
    topics = HotTopics.objects.all()
    trainings = Telim.objects.all()
    services = Service.objects.all()
    service = Service.objects.get(pk=id)
    events = Event.objects.all()
    context = {
        "events": events,
        "trainings": trainings,
        "services": services,
        "topics": topics,
        "general": general,
        "blogsmost": blogs,
        "socials": socials,
        "service": service,
        "categories": categories
    }
    return render(request, 'service.html', context)