from django.contrib import admin

# Register your models here.
from .models import Food, Consumed

admin.site.register(Food)
admin.site.register(Consumed)
