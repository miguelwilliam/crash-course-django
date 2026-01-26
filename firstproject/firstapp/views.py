from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello, world!</h1>")

class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Oi Etiópia!")