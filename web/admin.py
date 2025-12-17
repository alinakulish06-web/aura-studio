from django.contrib import admin
from .models import Service, News, Appointment

admin.site.register(Service)
admin.site.register(News)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # Додаємо 'message' у список відображення
    list_display = ('name', 'phone', 'message', 'service', 'created_at')
    readonly_fields = ('created_at',)