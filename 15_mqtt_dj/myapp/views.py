from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import djangoiot

# Create your views here.
class HomeView(View):

    def get(self, request, *args, **kwargs):
        new_broker = djangoiot.broker.register(host='localhost', port=1883)
        return HttpResponse("Hello World")

    