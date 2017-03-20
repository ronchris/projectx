from django.forms import ModelForm, Textarea
from collection.models import Review

class ReviewForm(ModelForm):
    class Meta:
		model = Review
		fields = [ 'user', 'rating', 'comment']
		widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 5})
        }