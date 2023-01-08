"""agriatraSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from agriatraSiteApp import views as mainViews
from host import views as hostViews
from guide import views as guideViews
from tourist import views as touristViews


urlpatterns = [
    path('', mainViews.index),  # landing page
    path('admin/', admin.site.urls),  # default admin page,
    path('hostFarmList/', hostViews.viewFarmList),
    path('registerHost/', hostViews.registerHost),
    path('registerGuide/', guideViews.registerGuide),
    path('registerTourist/', touristViews.registerTourist),
    path('loginGuide/', guideViews.loginGuide),
    path('loginTourist/', touristViews.loginTourist),
    path('loginHost/', hostViews.loginHost),
    path('aboutPage/', mainViews.aboutPage),
    path('viewTouristNFT/', touristViews.viewNFT),
    path('touristBeeKeeping/', touristViews.beeKeeping),
    path('farms/chandigarh', touristViews.chandigarhFarms),
    path('farms/visited/chandigarhVisited', touristViews.chandigarhFarmsVisited),
    path('viewHostProfile/', hostViews.viewProfile),
    path('manageHostAccommodations/', hostViews.manageAccommodations),
    path('login/', mainViews.login),
    path('register/', mainViews.register),
    path('accounts/', include('allauth.urls')),
]
