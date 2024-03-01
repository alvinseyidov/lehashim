from django.db import models



class General(models.Model):
    site_title = models.CharField(max_length=256)
    meta_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'Ümumi məlumatlar'

    class Meta:
        verbose_name = "Ümumi Məlumat"
        verbose_name_plural = "Ümumi Məlumat"


class Social(models.Model):
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    icon_white_backround = models.ImageField(null=True, blank=True)
    icon_black_backround = models.ImageField(null=True, blank=True)
    video_uzerinde_olsun = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sosial Media Hesabı"
        verbose_name_plural = "Sosial Media Hesabları"


class Featured(models.Model):
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.blog.title

    class Meta:
        verbose_name = "Seçilmiş Bloq"
        verbose_name_plural = "Seçilmiş Bloqlar"



class HotTopics(models.Model):
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = "Seçilmiş Mövzu"
        verbose_name_plural = "Seçilmiş Mövzular"




class Subscription(models.Model):
    email = models.CharField(max_length=256)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Abunə olmuş oxucu"
        verbose_name_plural = "Abunə olmuş oxucular"
