from django.contrib import admin

# Register your models here.
from .models import took , gave ,stats


class tookAdmin(admin.ModelAdmin):
    list_display = ( 'dataTime','amount', 'purpose',)



class gaveAdmin(admin.ModelAdmin):
    list_display = ( 'dataTime','amount', 'purpose',)
admin.site.register(took, tookAdmin)
admin.site.register(gave,gaveAdmin)
admin.site.register(stats)