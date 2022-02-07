from django.contrib import admin

# Register your models here.
from .models import Note, CustomUser

admin.site.register(Note)
admin.site.register(CustomUser)
