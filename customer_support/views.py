from django.shortcuts import render, get_object_or_404
from service_requests.models import ServiceRequest

def support_dashboard(request):
    all_requests = ServiceRequest.objects.all()
    return render(request, 'customer_support/dashboard.html', {'all_requests': all_requests})

def manage_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        if new_status == 'Resolved':
            service_request.resolved_at = timezone.now()
        service_request.save()
        return redirect('support_dashboard')
    return render(request, 'customer_support/request_management.html', {'service_request': service_request})