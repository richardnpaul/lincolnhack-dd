from django.db import models
from django.conf import settings
from mps.models import MP


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    mp = models.ForeignKey(MP, on_delete=models.CASCADE,)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    intro = models.TextField(null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
