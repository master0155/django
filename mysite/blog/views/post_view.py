from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        return HttpResponse("Hello, this is the Post View!")