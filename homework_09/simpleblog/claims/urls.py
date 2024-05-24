from django.urls import path, include

from .views import ShowProposal, profile_view, authView, home, about, logoutView, ClaimCreate

urlpatterns = [
    path("", home, name="home"),
    path('claims/<int:claim_pk>/', ShowProposal.as_view(), name='claim'),
    path("create/", ClaimCreate.as_view(), name="add_claim"),
    path("profile/", profile_view, name="profile"),
    path('signup/', authView, name="authView"),
    path('logout/', logoutView, name="logoutView"),
    path('about/', about, name="about"),
    path("__debug__/", include("debug_toolbar.urls")),
]
