from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    # 목록페이지 명칭 수정
    def changelist_view(self,request,extra_context=None):
        extra_context = {'title':'사용자 목록'}
        return super().changelist_view(request,extra_context)

    # 수정페이지 명칭 수정
    def changeform_view(self,request,object_id=None,form_url='',extra_context=None):
        fcuser = Fcuser.objects.get(pk = object_id)
        extra_context = {'title':f'{fcuser.email} 수정'}
        
        return super().changeform_view(request,object_id,form_url,extra_context)

admin.site.register(Fcuser,FcuserAdmin)
admin.site.site_header = '패스트 캠퍼스1'
admin.site.index_title = '패스트 캠퍼스2'
admin.site.site_title = '패스트 캠퍼스3'