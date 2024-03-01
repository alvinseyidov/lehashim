from django.db import models
from mptt.forms import TreeNodeChoiceField
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField



class Review(models.Model):
    full_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    feedback_short_version = models.TextField()
    feedback = models.TextField()
    profile_image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Rəy"
        verbose_name_plural = "Rəylər"

    def __str__(self):
        return self.full_name



class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.CharField(max_length=256, unique=True)
    class Meta:
        verbose_name = "Bloq teq"
        verbose_name_plural = "Bloq teqləri"

    def __str__(self):
        return self.name


class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,related_name="categories")
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    sort = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)



    class Meta:
        ordering = ('sort',)
        verbose_name = "Bloq kateqoriya"
        verbose_name_plural = "Bloq kateqoriyaları"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=256)
    reading_time = models.CharField(max_length=256)
    main_image = models.ImageField()
    short_description = models.TextField()
    description = RichTextUploadingField()
    cat = TreeForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    tags = models.ManyToManyField(Tag, blank=True, related_name="blogs")
    publish_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Bloq yazı"
        verbose_name_plural = "Bloq yazıları"
        ordering = ('-id',)


class SelectedBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.blog.title

    class Meta:
        verbose_name = "Seçilmiş Bloq yazı"
        verbose_name_plural = "Seçilmiş Bloq yazıları"
        ordering = ('sort',)
