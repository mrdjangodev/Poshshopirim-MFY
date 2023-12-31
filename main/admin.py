from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Worker
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    readonly_fields = ['password']
    list_display = ['id', 'first_name', 'last_name', 'phone', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'phone']

admin.site.register(Worker, WorkerAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)