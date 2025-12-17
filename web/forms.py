from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'name', 'phone', 'message']
        
        widgets = {
            'service': forms.Select(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Ваше ім'я"}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Номер телефону (0XX...)", 'type': 'tel'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'placeholder': "Додатковий коментар", 'rows': 3}),
        }

    # Перевірка Імені
    def clean_name(self):
        name = self.cleaned_data['name']
        # Якщо є щось крім букв і пробілів
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Неправильно вказано ім'я")
        return name

    # Перевірка Телефону (Тільки цифри + рівно 10 символів)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        
        # Перевірка 1: Чи тільки цифри?
        # Перевірка 2: Чи рівно 10 символів?
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Неправильно вказано номер")
            
        return phone