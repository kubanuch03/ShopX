from django.contrib import admin
from app_chat.models import *



class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['room','user','content','date_added']

admin.site.register(Room)
admin.site.register(Message)
