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
from django.contrib import admin
from django.urls import path
import recruit.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',recruit.views.HomeView.as_view(),name="home"),
    path('bftest/',recruit.views.BFTestView.as_view(),name='bftest'),
    path('bftest/result/',recruit.views.BFResultView.as_view(),name="bfresult"),
    path('history/', recruit.views.HistoryView.as_view(), name="history"),
    path('sglioninfo/', accounts.views.SglionInfoView.as_view(), name="sglioninfo"),
]
