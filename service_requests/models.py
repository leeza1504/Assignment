from django.db import models
from accounts.models import User

class RequestType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.request_type.name}"

class RequestAttachment(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')

    def __str__(self):
        return f"Attachment for {self.request.id}"