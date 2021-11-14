from django.urls import path

from askar.views import index

urlpatterns = [
    path('', index, name='home'),
]