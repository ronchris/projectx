from django.contrib import admin
from collection.models import Destination, Muni, Province, Upload, Review, Profile, Comment, Question

# set up automated slug creation
class DestinationAdmin(admin.ModelAdmin):
	model = Destination
	list_display = ('name', 'author', 'muni', 'province', 'address', 'description', 'features', 'activities', 'misc', 'coords',  'slug', 'user', 'image')
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

class ReviewAdmin(admin.ModelAdmin):
	model = Review
	list_display = ('destination', 'rating', 'user_name', 'comment', 'pub_date')
	list_filter = ['pub_date', 'user_name']
	search_fields = ['comment']
	
# and register it
admin.site.register(Review, ReviewAdmin)

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('user', 'review', 'bio', 'location', 'image')
	
# and register it
admin.site.register(Profile, ProfileAdmin)

class CommentAdmin(admin.ModelAdmin):
	model = Comment
	list_display = ('user', 'review', 'author', 'text', 'created_date')
	
# and register it
admin.site.register(Comment, CommentAdmin)

class QuestionAdmin(admin.ModelAdmin):
	model = Question
	list_display = ('destination', 'user_name', 'message', 'pub_date')
	list_filter = ['pub_date', 'user_name']
	search_fields = ['message']
	
# and register it
admin.site.register(Question, QuestionAdmin)
