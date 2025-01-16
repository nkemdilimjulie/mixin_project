from django.urls import path
from .views import MyRestrictedView




urlpatterns = [
    path("restricted/", MyRestrictedView.as_view(), name="restricted_view"),
]
