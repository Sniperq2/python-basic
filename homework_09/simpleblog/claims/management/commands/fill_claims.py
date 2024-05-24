import random

from django.core.management import BaseCommand
from django.utils import timezone

from .claims.models import Claim


class Command(BaseCommand):
    help = 'Fill some claims'

    def handle(self, *args, **options):
        Claim.objects.create(
            title="яма на дороге",
            status=random.randint(1, 5),
            created_date=timezone.now

        )
