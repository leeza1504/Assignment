from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='support_dashboard'),
    path('manage/<int:request_id>/', views.manage_request, name='manage_request'),
]