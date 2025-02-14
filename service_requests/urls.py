from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_service_request, name='create_request'),
    path('detail/<int:request_id>/', views.request_detail, name='request_detail'),
    path('tracking/', views.request_tracking, name='request_tracking'),
    path('incoming/', views.incoming_requests, name='incoming_requests'),
    path('update-status/<int:request_id>/', views.update_status, name='update_status'),
]