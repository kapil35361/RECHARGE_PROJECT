"""rechargeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from rechargeapp import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('airtel', views.Airtel_recharge)
router.register('vi', views.VI_recharge)
router.register('jio', views.Jio_recharge)
router.register('recharge', views.Mobilerecharge)

urlpatterns = [
    path('rechargeapp/',include(router.urls)),
    path('airtelrecha/<int:pk>/',views.Airtelrecharge),
    path('virecha/<int:pk>/',views.VIrecharge),
    path('jiorecha/<int:pk>/',views.Jiorecharge)
]    

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Airtellist.as_view()),
    path('vi/',views.VIlist.as_view()),
    path('jio/',views.Jiolist.as_view()),
]
'''