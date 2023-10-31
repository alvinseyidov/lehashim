from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,related_name="categories")
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    sort = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=256)
    reading_time = models.CharField(max_length=256)
    main_image = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()
    date = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True, related_name="blogs")

    def __str__(self):
        return self.title