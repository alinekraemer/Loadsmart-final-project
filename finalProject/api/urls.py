from django.urls import path
from finalProject.api import views


urlpatterns = [
    path('get-token/', views.get_token),
    path('carrier/list-available/', views.CarrierAvailableLoads.as_view({'get': 'list'})),
    path('carrier/list-accepted/', views.CarrierAcceptedLoads.as_view({'get': 'list'})),
    path('carrier/list-rejected/', views.CarrierRejectedLoads.as_view({'get': 'list'})),
    path('carrier/accept-load/<int:pk_load>/', views.CarrierAccept),
    path('carrier/reject-load/<int:pk_load>/', views.CarrierReject),
    path('carrier/drop-load/<int:pk_load>/', views.CarrierDrop),

]
