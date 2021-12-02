from django.contrib import admin
from .models import Hiretuber
# Register your models here.
class HiretubersAdmin(admin.ModelAdmin):
    list_display=('first_name', 'email', 'tuber_name')
    list_display_links=('first_name',)
    search_fields=('first_name', 'email')
    list_filter=('tuber_name',)

admin.site.register(Hiretuber, HiretubersAdmin)