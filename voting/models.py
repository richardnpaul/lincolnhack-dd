from django.db import models
from django.contrib.auth.models import User


class Bill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    result = models.BooleanField()
    status = models.BooleanField(default=False)

    def check_status(self):
        if self.status:
            self.result = self.results()
            self.save()

    def results(self):
        filtered_votes = Votes.objects.filter(bill=self.id)
        yay = filtered_votes.filter(vote=True).count
        nay = filtered_votes.filter(vote=False).count
        if yay > nay:
            return True
        elif nay > yay:
            return False

    def __str__(self):
        return self.name


class Votes(models.Model):
    vote = models.NullBooleanField()
    bill = models.ForeignKey(
        Bill, related_name='votes', on_delete=models.CASCADE)
    voter = models.ForeignKey(
        User, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.bill, self.voter)

    class Meta:
        unique_together = (('bill', 'voter'),)

