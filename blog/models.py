from django.db import models





class BlogCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=256)
    main_image = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True,related_name="blogs")

    def __str__(self):
        return self.title