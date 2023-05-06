from django.contrib import admin
from . import models

# Register your models here.

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'userId','createdOn')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section')


admin.site.register(models.AppInfo,AppAdmin)
admin.site.register( models.StudentInfo,StudentAdmin)

