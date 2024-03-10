from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home_view, name='home'),
    path('req/', leave_request_list, name='leave_request_list'),
    path('login/', login, name='login'),
    path('s/',user_signup,name='user_signup'),
    path('lo/',logout,name='logout'),
    path('h',newhomepage,name='newhomepage'),
    path('', leave_request_list, name='leave_request_list'),
    path('create/', create_leave_request, name='create_leave_request'),
    path('leave/', leave_request, name='leave_request'),

]

