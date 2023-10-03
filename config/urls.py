from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views as core_views
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name="index"),
    path('about/', core_views.about, name="about"),
    path('reviews/', core_views.reviews, name="reviews"),
    path('portfolio/', core_views.portfolio, name="portfolio"),
    path('category/<int:id>/', blog_views.category, name="category"),
    path('tag/<str:slug>/', blog_views.tag, name="tag"),
    path('blog/<int:id>/', blog_views.blog, name="blog"),
    path('contact/', core_views.contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)