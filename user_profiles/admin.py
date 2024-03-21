from django.contrib import admin
from .models import SellerProfile,CustomUser


admin.site.register(SellerProfile)

@admin.register(CustomUser)
class UserProfileAdmin(admin.ModelAdmin):
<<<<<<< HEAD
=======

>>>>>>> c3ddf98e65291b92b1d304bd5998061c19a2adeb
    list_display = ['email_or_phone','is_active',"is_seller","username"]
    list_filter = ["is_active",'is_seller']
    search_fields = ["is_seller"]
