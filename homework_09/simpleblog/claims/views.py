from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Claim


class ProposalListView(ListView):
    model = Claim
    context_object_name = 'claims'
    template_name = 'claims/claims_list.html'
    extra_context = {'title': 'Claims List'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowProposal(DetailView):
    model = Claim
    template_name = 'claims/claim.html'
    pk_url_kwarg = 'claim_pk'
    context_object_name = 'claim'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
