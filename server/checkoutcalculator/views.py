from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.conf import settings
from django.views.decorators.cache import never_cache
import os

from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


# Only allows GET
class ListItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
# Allows GET, PUT, PATCH
class DetailItem(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Code based on tutorial from https://dev.to/shakib609/deploy-your-django-react-js-app-to-heroku-2bck
# Serve Single Page Application
index = never_cache(TemplateView.as_view(template_name='index.html'))

# Code based on tutorial at https://librenepal.com/article/django-and-create-react-app-together-on-heroku/
# class FrontendAppView(View):
#     """
#     Serves the compiled frontend entry point
#     """
#     index_file_path = os.path.abspath(os.path.join(settings.BASE_DIR, os.pardir, 'react-build', 'index.html'))

#     def get(self, request):
#         try:
#             with open(self.index_file_path) as f:
#                 return HttpResponse(f.read())
#         except FileNotFoundError:
#             return HttpResponse(
#                 """
#                 This URL is only used when you have built the production
#                 version of the app.
#                 """,
#                 status=501,
#             )