from django.contrib import admin
from .models import Files
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class FileInline(admin.TabularInline):
    model = Files
    extra = 2

class MyUserAdmin(UserAdmin):
    #list_display = ('email', 'first_name', 'last_name')
    #list_filter = ('is_staff', 'is_superuser')
    inlines = [FileInline]


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
#admin.site.register(Files)
