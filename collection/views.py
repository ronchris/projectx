from django.shortcuts import get_object_or_404, render, redirect
from collection.models import Destination, Muni, Province, Review
from django.views.generic import View
from django.db.models import Q
from collection.forms import ReviewForm
import datetime


class IndexView(View):
	
	def get(self, request):
		
		destinations = Destination.objects.all()[:3]
		munis = Muni.objects.all()
		
		return render(request, 'index.html', {
		'destinations': destinations, 'munis': munis,
	})

def destination_detail(request, slug):
	
	destination = Destination.objects.get(slug=slug)
	uploads = destination.uploads.all()
	
	return render(request, 'destinations/destination_detail.html', {
	'destination': destination, 'uploads': uploads,
	})

def muni_detail(request, slug):
	
	muni = Muni.objects.get(slug=slug)
	destinations = muni.destination_set.all()
	
	return render(request, 'munis/muni_detail.html', {
	'muni': muni, 'destinations': destinations
	})

def province_detail(request, slug):
	
	province = Province.objects.get(slug=slug)
	munis = Muni.objects.all()
	
	return render(request, 'provinces/province_detail.html', {
	'province': province, 'munis': munis
	})

class DestinationSearchView(View):

    def get(self, request):
		search_text = request.GET.get('q')
		if search_text:
			destination = Destination.objects.filter(name__icontains=search_text).order_by('name')
			muni = Muni.objects.filter(name__istartswith=search_text).order_by('name')
			province = Province.objects.filter(name__istartswith=search_text).order_by('name')
			return render(request, 'ajax_search.html', {'destinations': destination,
				'munis': muni, 'provinces':province})
		return render(request, 'ajax_search.html', {})
	
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def add_review(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
		rating = form.cleaned_data['rating']
		comment = form.cleaned_data['comment']
		user = form.cleaned_data['user']
		review = Review()
		review.user = user
		review.destination = destination
		review.rating = rating
		review.comment = comment
		review.pub_date = datetime.datetime.now()
		review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('destinations/destination_detail', args=(destination.id,)))

    return render(request, 'destinations/destination_detail.html', {'destination': destination, 'form': form})
