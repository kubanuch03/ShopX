from django.contrib import admin
from .models import SellerProfile,CustomUser


admin.site.register(SellerProfile)

@admin.register(CustomUser)
class UserProfileAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['email_or_phone','is_active',"is_seller","username"]
=======
    list_display = ['email_or_phone','is_active',"is_seller"]
>>>>>>> e289b7570f0bcfeb760f1748f686c33f005fbb82
    list_filter = ["is_active",'is_seller']
    search_fields = ["is_seller"]
