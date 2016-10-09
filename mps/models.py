from django.db import models


class MP(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    profile = models.TextField(null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)