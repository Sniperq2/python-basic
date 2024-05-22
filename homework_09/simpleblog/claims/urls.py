from django.urls import path, include

from .views import ProposalListView, ShowProposal

urlpatterns = [
    path("", ProposalListView.as_view(), name="claims"),
    path('<int:claim_pk>/', ShowProposal.as_view(), name='claim'),
    path("__debug__/", include("debug_toolbar.urls")),
]
