from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone 
from .models import ServiceRequest
from .forms import ServiceRequestForm, AttachmentForm

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        attachment_form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid() and attachment_form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            attachment = attachment_form.save(commit=False)
            attachment.request = service_request
            attachment.save()
            return redirect('request_detail', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
        attachment_form = AttachmentForm()
    return render(request, 'service_requests/create_request.html', {'form': form, 'attachment_form': attachment_form})

def request_detail(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'service_requests/request_detail.html', {'service_request': service_request})

def request_tracking(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service_requests/request_tracking.html', {'user_requests': user_requests})

def incoming_requests(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service_requests/incoming_requests.html', {'requests': requests})

def update_status(request, request_id):
    if request.method == 'POST':
        service_request = get_object_or_404(ServiceRequest, id=request_id)
        new_status = request.POST.get('status')
        service_request.status = new_status
        if new_status == 'Resolved':
            service_request.resolved_at = timezone.now()
        service_request.save()
        messages.success(request, f'Status updated to {new_status} for request #{request_id}.')
    return redirect('incoming_requests')