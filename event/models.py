from django.db import models



class Event(models.Model):
    name = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name