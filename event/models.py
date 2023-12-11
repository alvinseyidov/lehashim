from django.db import models

class EventCategory(models.Model):
    name = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name



class Event(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="events")
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name