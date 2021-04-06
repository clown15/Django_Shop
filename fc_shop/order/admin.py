from django.contrib import admin
from django.utils.html import format_html
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display=('fcuser','product','quantity','styled_status')

    # obj는 각 개체
    # 커스텀필드
    def styled_status(self,obj):
        # '<b>'+{obj.status}+'</b>'
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == '결제완료':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return obj.status
    # table header text
    styled_status.short_description = '상태'


admin.site.register(Order,OrderAdmin)