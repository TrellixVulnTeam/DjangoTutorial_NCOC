"""djangotutorial1 URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from first_app import views as myapp_views
from django.conf.urls import handler404, handler500

urlpatterns = [
    #path('',views.index,name='index'),
    path('',include('first_app.urls')),
    path('api/',include('first_app.api.urls')),
    path('',include('User.urls')),
    path('admin/', admin.site.urls),
]

handler404 = myapp_views.error_404
handler500 = myapp_views.error_500