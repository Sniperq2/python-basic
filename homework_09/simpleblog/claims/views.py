from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm

from .models import Claim

class ShowProposal(DetailView):
    model = Claim
    template_name = 'claims/claim.html'
    pk_url_kwarg = 'claim_pk'
    context_object_name = 'claim'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def home (request):
    claims = Claim.objects.all()
    context = {'claims': claims }
    return render(request, 'claims/claims_list.html', context=context)


# @login_required
def profile_view(request):
    return render(request, 'user/profile.html')


def authView(request):
    if request.methos == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {"form": form})


def add_claim(request):
    return render(request, 'claims/create.html')


def about(request):
    return render(request, 'about.html', {})
