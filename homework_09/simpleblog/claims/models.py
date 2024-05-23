from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class ClaimStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ClaimType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Claim(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    moderation_till = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('ClaimStatus', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/claims/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('claims', kwargs={})

    def __str__(self):
        return self.title
