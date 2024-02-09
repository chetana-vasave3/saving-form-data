from django.contrib import admin

# Register your models here.
from saveform.models import Saveform
class saveformAdmin(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(Saveform,saveformAdmin)