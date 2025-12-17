from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from web import views  # <--- Обов'язково перевір цей рядок!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('news/', views.news, name='news'),
    path('contacts/', views.contacts, name='contacts'),
    path('booking/', views.booking, name='booking'), # <--- Ось наше нове посилання
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)