from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth import authenticate, login, logout

from .forms import AddClaimForm
from .models import Claim


class ShowProposal(DetailView):
    model = Claim
    template_name = 'claims/claim.html'
    pk_url_kwarg = 'claim_pk'
    context_object_name = 'claim'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def home(request):
    claims = Claim.objects.all()
    paginator = Paginator(claims, 2)

    page_number = request.GET.get("page")
    claims = paginator.get_page(page_number)
    return render(request, 'claims/claims_list.html', {"claims": claims})


# @login_required
def profile_view(request):
    return render(request, 'user/profile.html')


def logoutView(request):
    logout(request)
    messages.success(request, "Вы вышли из приложения")
    return redirect('home')


def authView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы зашли в приложение")
            return redirect("home")
        else:
            messages.success(request, "Ошибка логина")
            return redirect("login")
    else:
        return render(request, 'registration/login.html', {})


class ClaimCreate(LoginRequiredMixin, CreateView):
    model = Claim
    form_class = AddClaimForm
    template_name = 'claims/create.html'


def about(request):
    return render(request, 'about.html', {})
