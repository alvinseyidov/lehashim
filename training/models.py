from django.db import models

class TelimCategory(models.Model):
    name = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name



class Telim(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(TelimCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="telimler")
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name