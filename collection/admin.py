from django.contrib import admin
from collection.models import Destination

# set up automated slug creation
class DestinationAdmin(admin.ModelAdmin):
    model = Destination
    list_display = ('name', 'municipality', 'province', 'address', 'description', 'features', 'activities', 'misc', 'slug', 'user')
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Destination, DestinationAdmin)