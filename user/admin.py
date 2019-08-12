from django.contrib import admin
from .models import Suser
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Suser,userAdmin)