from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from leaflet.admin import LeafletGeoAdmin
from .models import LeakReport, Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'full_name',  'phone_number', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'full_name',  'phone_number')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(LeakReport)
class LeakReportAdmin(LeafletGeoAdmin):
    list_display = ('leak_type', 'customer_name', 'latitude', 'longitude', 'created_at')
    list_filter = ('leak_type',)
    search_fields = ('customer_name', 'description')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/map/', self.admin_site.admin_view(self.dashboard_view), name='admin_map_view'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        reports = LeakReport.objects.all()
        map_center = [0, 0]
        locations = []

        for report in reports:
            if report.latitude and report.longitude:
                locations.append({
                    'latitude': report.latitude,
                    'longitude': report.longitude,
                    'description': report.description,
                })
                map_center = [report.latitude, report.longitude]

        return render(request, 'admin/dashboard.html', {
            'locations': locations,
            'map_center': map_center,
        })



