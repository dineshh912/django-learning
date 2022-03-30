from django.urls import re_path, path
  
from . import consumers
  
websocket_urlpatterns = [
     path('ws/live/<int:id>', consumers.Calculator.as_asgi()),
]