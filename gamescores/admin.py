from gamescores.models import *
from django.contrib import admin

class CatanPlayerInline(admin.TabularInline):
	model = CatanPlayer
	extra = 6
	max_num = 6

class CatanGameAdmin(admin.ModelAdmin):
	inlines = [CatanPlayerInline]
	date_hierarchy = 'date_played'
	list_filter = ['date_played']

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(CatanGame, CatanGameAdmin)
admin.site.register(CatanPlayerStats)
