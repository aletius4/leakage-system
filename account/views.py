from django.shortcuts import render

# Create your views here.
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
