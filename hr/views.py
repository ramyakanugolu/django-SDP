from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LeaveRequest
from .forms import LeaveRequestForm

def create_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user.employee  # Assuming user is logged in and has an associated employee
            leave_request.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'create_leave_request.html', {'form': form})

def leave_request_list(request):
    leave_requests = LeaveRequest.objects.filter(employee=request.user.employee)  # Assuming user is logged in
    return render(request, 'leave_request_list.html', {'leave_requests': leave_requests})

