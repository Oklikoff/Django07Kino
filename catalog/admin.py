from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Genre)
# admin.site.register(Director)
# admin.site.register(Actor)
admin.site.register(AgeRate)
# admin.site.register(Status)
# admin.site.register(Kino)
admin.site.register(Country)

class Actoradmin(admin.ModelAdmin):
    list_display = ('fname','lname','born')#столбики в панели админа
    list_display_links = ('fname','lname')#работают
admin.site.register(Actor,Actoradmin)#регистрируем модель актер

class Directoradmin(admin.ModelAdmin):
    list_display = ('fname','lname')#столбики в панели админа
    list_display_links = ('fname','lname')#работают
admin.site.register(Director,Directoradmin)#регистрируем модель актер

class Kinoadmin(admin.ModelAdmin):
    list_display = ('title','year','director','display_actors')
    list_filter = ('status','genre','rating')
    fieldsets = (
        ('О фильме', {'fields': ('title', 'summary', 'actor')}),
        ('Рейтинг', {'fields': ('rating', 'ager', 'status')}),
        ('Остальное', {'fields': ('genre', 'country', 'director', 'year')})
    )
admin.site.register(Kino, Kinoadmin)

class Stinline(admin.TabularInline):
    model = Kino

class Statusadmib(admin.ModelAdmin):
    inlines = [Stinline]
admin.site.register(Status,Statusadmib)
