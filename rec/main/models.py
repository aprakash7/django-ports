from django.db import models

# Create your models here.


class commands(models.Model):
    cmd = models.CharField(max_length=30)
    repetition = models.IntegerField(null=True)
    gap = models.IntegerField()

    def __str__(self):
        return self.cmd
