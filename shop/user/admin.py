from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # admin페이지에 표시되는 내용
    list_display=("email","level")

admin.site.register(User,UserAdmin)