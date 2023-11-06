from django.db import models





class ServiceCategory(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="services")
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.name
