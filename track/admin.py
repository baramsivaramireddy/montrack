from django.contrib import admin

# Register your models here.
from .models import took , gave ,stats,expenses


class tookAdmin(admin.ModelAdmin):
    list_display = ( 'dataTime','amount', 'purpose',)


class expenseAdmin(admin.ModelAdmin):
    list_display = ( 'dataTime','amount', 'purpose',)

class gaveAdmin(admin.ModelAdmin):
    list_display = ( 'dataTime','amount', 'purpose',)
admin.site.register(took, tookAdmin)
admin.site.register(gave,gaveAdmin)
admin.site.register(stats)

admin.site.register(expenses,expenseAdmin)