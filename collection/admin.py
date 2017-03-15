from django.contrib import admin
from collection.models import Destination, Muni, Province, Upload

# set up automated slug creation
class DestinationAdmin(admin.ModelAdmin):
    model = Destination
list_display = ('name', 'municipality', 'province', 'address', 'description', 'features', 'activities', 'misc', 'coords',  'slug', 'user', 'image')
prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Destination, DestinationAdmin,)

class UploadAdmin(admin.ModelAdmin):
	list_display = ('destination',)
	list_display_links = ('destination',)

# and register it
admin.site.register(Upload, UploadAdmin,)

class MuniAdmin(admin.ModelAdmin):
    model = Muni
list_display = ('name', 'address', 'accessibility', 'description', 'safety_rating', 'population', 'known_for', 'misc', 'activities', 'features',  'coords',  'slug', 'image')
prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Muni, MuniAdmin)

class ProvinceAdmin(admin.ModelAdmin):
    model = Province
list_display = ('name', 'address', 'description', 'coords',  'slug', 'image')
prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Province, ProvinceAdmin)