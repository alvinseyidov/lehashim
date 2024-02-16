from django.db import models
from mptt.forms import TreeNodeChoiceField
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField




class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.CharField(max_length=256, unique=True)

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
    main_image = models.ImageField()
    short_description = models.TextField()
    description = RichTextUploadingField()
    cat = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="blogs")
    tags = models.ManyToManyField(Tag, blank=True, related_name="blogs")
    publish_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title