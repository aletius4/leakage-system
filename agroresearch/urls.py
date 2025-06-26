from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),
    path('geographical_information_system/', views.geographical_information_system, name='geographical_information_system'),
    path('remote-sensing/', views.remote_sensing, name='remote_sensing'),
    path('report_leak/', views.report_leak, name='report_leak'),
    path('leak_report_success/', views.leak_report_success, name='leak_report_success'),
    path('view_leaks/', views.view_leaks, name='view_leaks'),
    path('admin_map/', views.admin_map_view, name='admin_map_view'),
    path('admin_leak_list/', views.admin_dashboard, {'view_type': 'leak_list'}, name='admin_leak_list'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard_view'),
]

