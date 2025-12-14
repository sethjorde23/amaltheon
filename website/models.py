from django.db import models


class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    message = models.TextField()

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class DemoRequest(models.Model):
    SEGMENT_CHOICES = [
        ('grower', 'Grower'),
        ('processor', 'Food Processor'),
        ('cpg', 'CPG Producer'),
        ('restaurant', 'Restaurant / Foodservice'),
        ('government', 'Government / Institution'),
        ('investor', 'Investor'),
        ('ag_supply', 'Ag Supply / Input Supplier'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('scheduled', 'Demo Scheduled'),
        ('completed', 'Demo Completed'),
        ('closed', 'Closed'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    segment = models.CharField(max_length=50, choices=SEGMENT_CHOICES)
    goals = models.TextField(blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True, help_text='Internal notes about this lead')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Demo Request'
        verbose_name_plural = 'Demo Requests'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company}"