from django.http import HttpResponseNotAllowed

#    class RestrictMethodsMixin:
#        allowed_methods = ['GET']  # Default to only allow GET requests
# ????????
   
# http_restrictor/mixins.py

from django.http import HttpResponseNotAllowed

class RestrictMethodsMixin:
    allowed_methods = ['GET']  # Default to only allow GET requests

    def dispatch(self, request, *args, **kwargs):
                
        if request.method not in self.allowed_methods:
                return HttpResponseNotAllowed(self.allowed_methods)
        return super().dispatch(request, *args, **kwargs)