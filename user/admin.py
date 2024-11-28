from django.contrib import admin
from user.models import User, User_Address

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(User, UserAdmin)
admin.site.register(User_Address)
