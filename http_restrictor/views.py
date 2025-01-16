# from django.shortcuts import render

#    from django.http import HttpResponse
#    from django.views import View
#    from .mixins import RestrictMethodsMixin

#  ????
from django.views.generic import View
from django.http import HttpResponse
from django.views import View
from .mixins import RestrictMethodsMixin

# Create your views here.

class MyRestrictedView(RestrictMethodsMixin, View):
    allowed_methods = ["GET", "POST"]  # Allow only GET and POST requests

    def get(self, request, *args, **kwargs):
        # Handle GET request
        return HttpResponse("This is a GET request.")

    def post(self, request, *args, **kwargs):
        # Handle POST request
        return HttpResponse("This is a POST request.")
