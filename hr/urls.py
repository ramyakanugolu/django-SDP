from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_leave_request, name='create_leave_request'),
    path('list/', views.leave_request_list, name='leave_request_list'),
]