from .forms import AppointmentForm
from django.shortcuts import redirect

from django.shortcuts import render
from .models import Service, News

def index(request):
    # Беремо всі послуги з бази даних
    services = Service.objects.all()
    # Беремо всі новини з бази даних
    news = News.objects.all()

    # Передаємо їх у шаблон index.html
    return render(request, 'web/index.html', {
        'services': services,
        'news': news
    })

def contacts(request):
    return render(request, 'web/contacts.html')

def services(request):
    # Фільтруємо послуги по категоріях
    nails = Service.objects.filter(category='nails')
    brows = Service.objects.filter(category='brows')
    massage = Service.objects.filter(category='massage')
    cosmetology = Service.objects.filter(category='cosmetology')
    hair = Service.objects.filter(category='hair')

    return render(request, 'web/services.html', {
        'nails': nails,
        'brows': brows,
        'massage': massage,
        'cosmetology': cosmetology,
        'hair': hair,
    })

def news(request):
    all_news = News.objects.all()
    return render(request, 'web/news.html', {'news': all_news})

def booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'web/success.html') # Покажемо сторінку успіху
    else:
        form = AppointmentForm()

    return render(request, 'web/booking.html', {'form': form})