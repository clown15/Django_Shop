from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Fcuser,FcuserAdmin)
admin.site.site_header = '패스트 캠퍼스1'
admin.site.index_title = '패스트 캠퍼스2'
admin.site.site_title = '패스트 캠퍼스3'