"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from UrbanDjango.task2.views import f_view, cl_view
from UrbanDjango.task4.views import game, cart, game_platform
from UrbanDjango.task5.views import sign_up_by_django, sign_up_by_html
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', f_view),
    path('', cl_view),
    path('platform/', game_platform),
    path('platform/games/', game),
    path("platform/cart/", cart),
    path("html_forms/", sign_up_by_html),
    path("django_forms", sign_up_by_django)
    ]
