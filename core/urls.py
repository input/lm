"""
URL configuration for core project.

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
import djp

from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('blog.urls')),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('admin/', admin.site.urls),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('examples/', include('examples.urls')),
    path('portfolio', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
] + djp.urlpatterns()
