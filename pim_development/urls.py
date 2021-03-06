"""pim_development URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
#from django.views.generic.simple import direct_to_template
#from django.views import views
from django.views.generic.base import TemplateView
#from django.core.urlresolvers import reverse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dashboard.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login', auth_views.login),
    path('logout', auth_views.logout),
    path('currencies/', include('currencies.urls')),

    #path('/',views.index, name='index'),
    #path('', direct_to_template,{'template': 'registration.html' }, 'index'),
    #path('/', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('', views.index, name='index'),
]
