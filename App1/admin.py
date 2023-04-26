from django.contrib import admin

from . import models

# Register your models here.

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'userId','createdOn')


admin.site.register( models.AppInfo,AppAdmin)