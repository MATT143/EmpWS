
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('post/task/details/to/ews/',getTaskDetails.as_view()),
    path('',home,name='home'),
    path('expert/home',expertHome,name='expert-home'),
    path('expert/register',registerPage,name='register'),

    path('profile/',profileView,name='profile'),
    path('expert/dashboard',expertDashBoard,name='dashboard'),
    #
    path('expert/login',LoginView.as_view(template_name='expertapp/login.html'),name='login'),
    path('expert/logout',LogoutView.as_view(template_name='expertapp/logout.html'),name='logout'),
    # path('expert/verify/bank',verifyBankAccount,name='verify-bank'),

    # path('task/status/sync/back',taskStatusSyncBack.as_view(),name='status-sync'),
    # path('expert/task/details/<uuid:pk>',TicketDetailView.as_view(template_name='custws/ticket_detail.html'),name='ticket-detail'),

]
