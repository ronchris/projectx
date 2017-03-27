from django.shortcuts import get_object_or_404, render, redirect
from django import http
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from collection.models import Destination, Muni, Province, Review, Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.db.models import Q
from collection.forms import ReviewForm, UserForm, ProfileForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import Http404
from django.db import transaction
import json
import datetime


class IndexView(View):
	
	def get(self, request):
		
		destinations = Destination.objects.all()[:3]
		munis = Muni.objects.all()
		
		return render(request, 'index.html', {
		'destinations': destinations, 'munis': munis,
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
	
def destination_detail(request, slug, profile_id=None):
	
	destination = Destination.objects.get(slug=slug)
	uploads = destination.uploads.all()
	profiles = Profile.objects.all()
	form = ReviewForm()
	print form
	
	return render(request, 'destinations/destination_detail.html', {
	'destination': destination, 'uploads': uploads, 'form': form, 'profiles': profiles
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

def profile_detail(request, profile_id=None):
	
	id = request.user.id
	review = None
	if profile_id:
		reviews = Review.objects.filter(user_name_id=profile_id)
		print reviews
		id = profile_id
			
	profile = Profile.objects.get(user_id=id)
	print profile.location
	print profile.user.username
	reviews = Review.objects.all()
	
	return render(request, 'profiles/profile_detail.html', {
	'profile': profile, 'reviews': reviews, 'user': request.user
	})

@login_required
def add_review(request, destination_id):
	
	destination = get_object_or_404(Destination, pk=destination_id)
	user_posted = False
	if request.method=='POST':
		form = ReviewForm(request.POST) 
		
		if form.is_valid():
			rating = form.cleaned_data['rating']
			comment = form.cleaned_data['comment']
			user_name = request.user
			review = Review()
			review.user_name = user_name
			review.destination = destination
			review.rating = rating
			review.comment = comment
			review.pub_date = datetime.datetime.now()
			review.save()
			user_posted = True
		else:
			messages.error(request, "Error")
	return redirect('destination_detail', slug=destination.slug)


@login_required
@transaction.atomic
def update_profile(request):
	
	created = Profile.objects.get_or_create(user=request.user)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, ('Your profile was successfully updated!'))
			return redirect('/profiles/')
		else:
			messages.error(request, ('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
    		return render(request, 'profiles/profile_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

class DeleteReview(View):
	print 'delete_review'
	def get_object(self, id):
		try:
			return Review.objects.get(id=id)
		except Review.DoesNotExist:
			raise Http404
	
	def get(self, request):
		review_id = request.GET.get("reviewId")
		print "review"
		print review_id
		if review_id:
			review = get_object_or_404(Review, id=review_id)
			if review.user_name_id == request.user.id:
				review.delete()
				message = {"status": "success", "message":  "review deleted" }
			else:
				message = {"status": "error", "message":  "invalid user" }
		else:
			message = {"status": "error", "message":  "review id not found" }
			
		return http.HttpResponse(json.dumps(message), content_type="application/json")
								 
	