from django import forms
from .models import ServiceRequest, RequestAttachment

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = RequestAttachment
        fields = ['file']