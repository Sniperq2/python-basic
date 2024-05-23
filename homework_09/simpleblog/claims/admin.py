from django.contrib import admin

from .models import Claim, ClaimStatus, ClaimType

admin.site.register(Claim)
admin.site.register(ClaimStatus)
admin.site.register(ClaimType)
