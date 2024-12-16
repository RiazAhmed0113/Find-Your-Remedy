from django.db import models


# Create your models here.
class Illness(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = [
            'name',
        ]
        verbose_name_plural = 'Illnesses'

    def __str__(self):
        return self.name
