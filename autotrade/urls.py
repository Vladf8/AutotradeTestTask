from django.urls import path
from .views import create_dealer, delete_dealer, update_dealer, get_dealer, delete_auto, get_auto, create_auto, update_auto

urlpatterns = [
    path('dealer/create/', create_dealer),
    path('dealer/delete/', delete_dealer),
    path('dealer/update/', update_dealer),
    path('dealer/get/', get_dealer),
    path('auto/create/', create_auto),
    path('auto/delete/', delete_auto),
    path('auto/update/', update_auto),
    path('auto/get/', get_auto),
]