from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('nails', 'Нігтьовий сервіс'),
        ('brows', 'Брови та Вії'),
        ('massage', 'Масаж'),
        ('cosmetology', 'Косметологія'),
        ('hair', 'Перукарське мистецтво'),
    ]

    title = models.CharField(max_length=200, verbose_name="Назва послуги")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='nails', verbose_name="Категорія")
    price = models.CharField(max_length=50, verbose_name="Ціна")
    description = models.TextField(verbose_name="Опис", blank=True)
    image = models.ImageField(upload_to='services/', verbose_name="Фото", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок новини")
    text = models.TextField(verbose_name="Текст новини")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    image = models.ImageField(upload_to='news/', verbose_name="Фото", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

class Appointment(models.Model):
    # Ось тут ми зв'язуємо заявку з послугою
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name="Послуга")
    
    name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    message = models.TextField(verbose_name="Коментар", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Заявка на запис"
        verbose_name_plural = "Заявки на запис"