"""recruit2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import recruit.views
import accounts.views
import apply.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',recruit.views.HomeView.as_view(),name="home"),
    path('bftest/',recruit.views.BFTestView.as_view(),name='bftest'),
    path('bftest/result/',recruit.views.BFResultView.as_view(),name="bfresult"),
    path('history/', recruit.views.HistoryView.as_view(), name="history"),
    path('sglioninfo/', accounts.views.SglionInfoView.as_view(), name="sglioninfo"),
    path('accounts/',include('allauth.urls')),
    path('socialregister/', accounts.views.SocialregisterView.as_view(),name="socialregister"),
    url(r'^traffic/', include('traffic_monitor.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)