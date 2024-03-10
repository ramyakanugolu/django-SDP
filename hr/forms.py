from django import forms
from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['reason', 'start_date', 'end_date']
