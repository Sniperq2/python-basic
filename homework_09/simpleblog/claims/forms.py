from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Claim


class ClaimCreate(LoginRequiredMixin, CreateView):
    model = Claim
    fields = ["title", "text", "created_date", "moderation_till", "image"]
    template_name = 'claims/create.html'
