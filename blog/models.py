from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=256)
    main_image = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title