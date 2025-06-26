from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, AccountUpdateForm, AccountAuthenticationForm, LeakReportForm
from django.http import HttpResponse, JsonResponse
from .models import LeakReport
import json

# Ukurasa wa nyumbani
def home_view(request):
    return render(request, 'home.html')


# Ukurasa wa kuhusu
def about(request):
    return render(request, 'about.html')

# Ukurasa wa mawasiliano
def contact(request):
    return render(request, 'contact.html')

# Ukurasa wa Application
def application(request):
    return render(request, 'application.html')

# Ukurasa wa Geographic Information System
def geographical_information_system(request):
    return render(request, 'geographical_information_system.html')

# Ukurasa wa Remote Sensing
def remote_sensing(request):
    return render(request, 'remote_sensing.html')


# Registration View
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.full_name = form.cleaned_data.get("full_name")
            user.phone_number = form.cleaned_data.get("phone_number")
            password1 = form.cleaned_data.get("password1")
            if password1:
                user.set_password(password1)
            user.save()

            email = form.cleaned_data.get("email")
            user = authenticate(email=email, password=password1)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {"form": form})


# Login View
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect("login")
    return render(request, "login.html")


# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')


# Account Update View
@login_required
def account_view(request):
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("account")
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, "account.html", {"account_form": form})


# Report Leak
@login_required
def report_leak(request):
    if request.method == 'POST':
        form = LeakReportForm(request.POST)
        if form.is_valid():
            leak_report = form.save(commit=False)
            leak_report.customer = request.user
            lat = request.POST.get('latitude')
            lon = request.POST.get('longitude')

            # Hakikisha zipo kabla ya ku-convert
            if lat and lon:
                try:
                    leak_report.latitude = float(lat)
                    leak_report.longitude = float(lon)
                except ValueError:
                    messages.error(request, 'Lat/Long sio halali.')
                    return redirect('report_leak')
            else:
                messages.error(request, 'Location haikupatikana. Tafadhali ruhusu browser kutumia location yako.')
                return redirect('report_leak')

            leak_report.save()
            messages.success(request, 'Ripoti yako ya hitilafu imewasilishwa kwa mafanikio!')
            return redirect('leak_report_success')
        else:
            messages.error(request, 'Tafadhali jaza taarifa zote kikamilifu.')
    else:
        form = LeakReportForm()
    return render(request, 'report_leak.html', {'form': form})

def leak_report_success(request):
    return render(request, 'leak_report_success.html')


# View all leaks
@login_required
def view_leaks(request):
    leak_reports = LeakReport.objects.all()
    return render(request, 'view_leakage.html', {'leak_reports': leak_reports})


# Admin dashboard - switchable views
def admin_dashboard(request, view_type=None):
    leakage = LeakReport.objects.all()
    if view_type == 'map':
        return render(request, 'admin_map.html', {'leakage': leakage, 'view_type': 'map'})
    elif view_type == 'leak_list':
        return render(request, 'admin_leak_list.html', {'leakage': leakage, 'view_type': 'leak_list'})
    return render(request, 'admin_dashboard.html', {'leakage': leakage, 'view_type': 'default'})

# Admin leak list
def admin_leak_list(request):
    leak = LeakReport.objects.all()
    return render(request, 'admin_leak_list.html', {'leak': leak})


from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from .models import LeakReport
import json

def admin_map_view(request):
    leak = LeakReport.objects.all().values(
        'latitude', 'longitude', 'description',
    )
    leak_json = json.dumps(list(leak), cls=DjangoJSONEncoder)
    return render(request, 'admin_map.html', {'leakage_json': leak_json})


