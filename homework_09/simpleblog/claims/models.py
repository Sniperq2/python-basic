from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Claim(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    moderation_till = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('ClaimStatus', on_delete=models.PROTECT)
    type = models.ForeignKey('ClaimType', on_delete=models.PROTECT)
    image = models.ForeignKey('Images', on_delete=models.PROTECT)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('claims', kwargs={})

    def __str__(self):
        return self.title

class ClaimStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class ClaimType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    path = models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
