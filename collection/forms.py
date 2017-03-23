from django.forms import ModelForm, Textarea
from collection.models import Review, Profile
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = [ 'rating', 'comment']
		widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5})
        }
	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['rating'].error_messages = {'required': 'Please enter a rating.'}
		self.fields['comment'].error_messages = {'required': 'Please enter a review.'}

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
		model = Profile
		fields = ('bio', 'location', 'image')