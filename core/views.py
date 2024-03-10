from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.models import *
from blog.models import Category as Category, Blog, Tag, Review, SelectedBlog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from event.models import Event
from service.models import Service
from training.models import Telim
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    categories = Category.objects.filter(parent__isnull=True)
    featured = Featured.objects.all()
    topics = HotTopics.objects.all()
    general = General.objects.all()
    blogs = Blog.objects.all()
    bestblogs = Blog.objects.all().order_by('-views')[:3]
    blogsf = SelectedBlog.objects.all()[:3]
    blogsfmobile = SelectedBlog.objects.all()[:1]
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
    events = Event.objects.all()
    reviews = Review.objects.all()
    context = {
        "bestblogs": bestblogs,
        "reviews": reviews,
        "events": events,
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
    events = Event.objects.all()
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
        "events": events,
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
    events = Event.objects.all()
    reviews = Review.objects.all()
    review_count = reviews.count()//3
    reviews1 = reviews[:review_count]
    reviews2 = reviews[review_count:2*review_count]
    reviews3 = reviews[2*review_count:]
    context = {
        "reviews1": reviews1,
        "reviews2": reviews2,
        "reviews3": reviews3,
        "events": events,
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
    events = Event.objects.all()
    context = {
        "events": events,
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
    events = Event.objects.all()
    context = {
        "events": events,
        "trainings": trainings,
        "services": services,
        "topics": topics,
        "general": general,
        "socials": socials,
        "categories": categories
    }
    return render(request, 'contact.html', context)



class SignUpForm(UserCreationForm):
#profile_year        = blaaa blaa blaaa irrelevant.. You have your own stuff here don't worry about it

   # here is the important part.. add a class Meta-
   class Meta:
      model = User #this is the "YourCustomUser" that you imported at the top of the file
      fields = ('email', 'full_name','password1', 'password2',)

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    categories = Category.objects.filter(parent__isnull=True)
    general = General.objects.all()
    socials = Social.objects.all()
    blogs = Blog.objects.all()[:4]
    topics = HotTopics.objects.all()
    trainings = Telim.objects.all()
    services = Service.objects.all()
    events = Event.objects.all()
    reviews = Review.objects.all()
    extra_context = {
        "reviews": reviews,
        "events": events,
        "trainings": trainings,
        "services": services,
        "topics": topics,
        "general": general,
        "blogsmost": blogs,
        "socials": socials,
        "categories": categories
    }

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        is_exist = Subscription.objects.filter(email=email)
        if not is_exist:
            Subscription.objects.create(email=email)
        categories = Category.objects.filter(parent__isnull=True)
        featured = Featured.objects.all()
        topics = HotTopics.objects.all()
        general = General.objects.all()
        tags = Tag.objects.all()[:6]
        socials = Social.objects.all()



        trainings = Telim.objects.all()
        services = Service.objects.all()
        events = Event.objects.all()
        reviews = Review.objects.all()

        context = {
            "reviews": reviews,
            "events": events,
            "trainings": trainings,
            "services": services,
            "tags": tags,
            "topics": topics,
            "general": general,
            "featured": featured,
            "socials": socials,
            "categories": categories
        }
        return render(request, 'success.html', context)




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
    events = Event.objects.all()
    context = {
        "events": events,
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

def event(request, id):
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
    events = Event.objects.all()
    context = {
        "events": events,
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
    events = Event.objects.all()
    context = {
        "events": events,
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