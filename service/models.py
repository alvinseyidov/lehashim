from django.db import models





class Service(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name
