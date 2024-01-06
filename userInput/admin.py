from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("first_name","user_phone_number","rating")
    list_filter =("first_name","rating")

admin.site.register(Review,ReviewAdmin)
