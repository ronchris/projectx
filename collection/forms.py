from django.forms import ModelForm, Textarea
from collection.models import Review


class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = [ 'rating', 'comment']
		widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5})
        }
	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['rating'].error_messages = {'required': ''}
		self.fields['comment'].error_messages = {'required': ''}
		