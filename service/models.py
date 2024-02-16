from django.db import models





class Service(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"

    def __str__(self):
        return self.name
