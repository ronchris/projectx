from django.forms import ModelForm, Textarea
from collection.models import Review, Profile, Comment
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = [ 'rating', 'comment']
		widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5, 'placeholder': 'What would you like to say?', 'required': True}),
        }
	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['comment'].label = "Review"
#		self.fields['rating'].error_messages = {'required': 'Please enter a rating.'}
#		self.fields['comment'].error_messages = {'required': 'Please enter a review.'}
		

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
		model = Profile
		fields = ('bio', 'location', 'image')

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['text']
		widgets = {
            'text': Textarea(attrs={'cols': 40, 'rows': 2, 'placeholder': 'Ask a question or leave a comment!', 'required': True}),
        }
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['text'].error_messages = {'required': 'Please enter a comment.'}