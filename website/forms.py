from django import forms
from .models import ContactSubmission, DemoRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['first_name', 'last_name', 'email', 'company', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'company': forms.TextInput(),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'required': True,
                'placeholder': 'Tell us what you\'re looking for...'
            }),
        }


class DemoRequestForm(forms.ModelForm):
    class Meta:
        model = DemoRequest
        fields = ['first_name', 'last_name', 'email', 'company', 'role', 'segment', 'goals']
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'company': forms.TextInput(attrs={'required': True}),
            'role': forms.TextInput(attrs={'placeholder': 'e.g., Operations Manager'}),
            'segment': forms.Select(attrs={'required': True}),
            'goals': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Tell us about your goals or challenges...'
            }),
        }