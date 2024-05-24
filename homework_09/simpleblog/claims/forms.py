from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from .models import Claim, ClaimType, ClaimStatus


class AddClaimForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Claim
        fields = ["author", "title", "text", "created_date", "moderation_till", "image", "status"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 20}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

    def form_valid(self, form):
        status = get_object_or_404(ClaimStatus, pk=1)
        form.instance.status = status
        return super(AddClaimForm, self).form_valid(form)
