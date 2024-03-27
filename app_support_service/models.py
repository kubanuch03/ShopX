from django.db import models
from user_profiles.models import CustomUser as User


class SupportService(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    instagram_link = models.URLField()
    whatsapp_link = models.URLField()
    facebook_link = models.URLField()
    telegram_token = models.CharField(max_length=50)
    telegram_chat_id = models.CharField(max_length=15)

    def __str__(self):
        return "Служба поддержки"

