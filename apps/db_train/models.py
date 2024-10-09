from django.db import models

# Создайте свои модели здесь


class Author(models.Model):
    username = models.SlugField()
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('м', 'мужской'), ('ж', 'женский')])
    self_esteem = models.DecimalField(max_digits=2, decimal_places=1)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.IntegerField(null=True, editable=False)
    date_birth = models.DateField()
    status_rule = models.BooleanField()
    image = models.ImageField(upload_to='foto_profile')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
