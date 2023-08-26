from django.db import models



class General(models.Model):
    site_title = models.CharField(max_length=256)
    meta_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'Ümumi məlumatlar'


class Social(models.Model):
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Featured(models.Model):
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.blog.title