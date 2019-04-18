from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from finalProject.core import views

router = routers.DefaultRouter()
router.register(r'loads', views.LoadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('account/', include('finalProject.account.urls'), name='account'),
    path('api/', include('finalProject.api.urls'), name="api"),
    path('carrier/', include('finalProject.carrier.urls'), name='carrier'),
    path('shipper/', include('finalProject.shipper.urls'), name='shipper'),
]