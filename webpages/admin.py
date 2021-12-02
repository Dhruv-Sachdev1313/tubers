from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))


    list_display = ('id','myphoto', 'first_name', 'role_name', 'created_date')
    list_display_links = ('first_name', 'id',)
    search_fields = ('first_name', 'role_name')
    list_filter = ('role_name',)

class SliderAdmin(admin.ModelAdmin):
    def slider_photo(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))
    
    list_display = ('headline', 'slider_photo', 'button_text')


admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
