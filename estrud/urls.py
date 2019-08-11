"""estrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home import urls as home_urls
from pdelta import urls as pdelta_urls
from int_analitica import urls as int_analitica_urls
from int_numerica import urls as int_numerica_urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(home_urls)),
    path('int-analitica/', include(int_analitica_urls)),
    path('int-numerica/', include(int_numerica_urls)),
    path('pdelta/', include(pdelta_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin-django/', admin.site.urls),
]
