# gas_utility_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('service/', include('service_requests.urls')),
    path('support/', include('customer_support.urls')),
    path('', RedirectView.as_view(url='/accounts/profile/')),
]