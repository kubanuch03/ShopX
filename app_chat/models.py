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



from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    users = models.ManyToManyField(User, related_name='rooms')

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.room}'
    class Meta:
        ordering = ('date_added',)



