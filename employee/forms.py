from django import forms
from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker'}),

        }

class LeaveForm(forms.Form):
    leave_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

from django import forms
from .models import Employee

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    roles = forms.ChoiceField(choices=[('role1', 'Role 1'), ('role2', 'Role 2')])

    class Meta:
        model = Employee
        fields = ['username', 'password', 'confirm_password', 'roles']

from django import forms
from .models import LeaveRequest





