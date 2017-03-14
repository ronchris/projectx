from django.shortcuts import render
from collection.models import Destination, Muni, Province
from django.views.generic import View
from django.db.models import Q


class IndexView(View):
	
	def get(self, request):
		destinations = Destination.objects.all()
		munis = Muni.objects.all()
		return render(request, 'index.html', {
		'destinations': destinations, 'munis': munis,
	})

def destination_detail(request, slug):
	destination = Destination.objects.get(slug=slug)
	
	uploads = destination.uploads.all()
	
	return render(request, 'destinations/destination_detail.html', {
	'destination': destination, 'uploads' : uploads,
		
	})

def muni_detail(request, slug):
	muni = Muni.objects.get(slug=slug)
	
	return render(request, 'munis/muni_detail.html', {
	'muni': muni,
	})

def province_detail(request, slug):
	province = Province.objects.get(slug=slug)
	
	return render(request, 'provinces/province_detail.html', {
	'province': province,
	})

class DestinationSearchView(View):

    def get(self, request):
		search_text = request.GET.get('q')
		if search_text:
			destination = Destination.objects.filter(Q(province__istartswith=search_text)|Q(name__istartswith=search_text)|Q(municipality__istartswith=search_text)|Q(address__icontains=search_text)).order_by('name')
			return render(request, 'ajax_search.html', {'destinations': destination})
		return render(request, 'ajax_search.html', {})


