from django.db import models




class Telim(models.Model):
    name = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort',)
        verbose_name = "Təlim"
        verbose_name_plural = "Təlimlər"

    def __str__(self):
        return self.name