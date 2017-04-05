from django.shortcuts import get_object_or_404, render, redirect
from django import http
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from collection.models import Destination, Muni, Province, Review, Profile, Comment, Question, CommentQ
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.db.models import Q
from collection.forms import ReviewForm, UserForm, ProfileForm, CommentForm, QuestionForm, CommentQForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import Http404
from django.db import transaction
from django.utils import timezone
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
	comments = Comment.objects.all()
	commentqs = CommentQ.objects.all()
	question = Question.objects.all()
	form = ReviewForm()
	comment_form = CommentForm()
	commentq_form = CommentQForm()
	question_form = QuestionForm()
	
	return render(request, 'destinations/destination_detail.html', {
	'destination': destination, 'uploads': uploads, 'form': form, 'profiles': profiles, 'comments': comments, 'comment_form': comment_form, 'question_form': question_form, 'commentq_form': commentq_form, 'commentqs': commentqs
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
	reviews = Review.objects.filter(user_name_id=profile_id)
	
	return render(request, 'profiles/profile_detail.html', {
	'profile': profile,  'reviews': reviews, 'user': request.user
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
def add_question(request, destination_id):
	
	destination = get_object_or_404(Destination, pk=destination_id)
	user_posted = False
	if request.method=='POST':
		question_form = QuestionForm(request.POST) 
		
		if question_form.is_valid():
			message = question_form.cleaned_data['message']
			user_name = request.user
			question = Question()
			question.user_name = user_name
			question.destination = destination
			question.message = message
			question.pub_date = datetime.datetime.now()
			question.save()
			user_posted = True
		else:
			messages.error(request, "Error")
	return redirect('destination_detail', slug=destination.slug)


@login_required
def update_profile(request):
	
	profile = Profile.objects.all()
	created = Profile.objects.get_or_create(user=request.user)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST,  request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, ('Your profile was successfully updated!'))
			return redirect('profile_detail', profile_id=request.user.id)
		else:
			messages.error(request, ('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
    		return render(request, 'profiles/profile_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form, 'profile': profile
    })

		
class DeleteReview(View):
	print 'delete_comment'
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

	
class DeleteQuestion(View):
	print 'delete_comment'
	def get_object(self, id):
		try:
			return Question.objects.get(id=id)
		except Review.DoesNotExist:
			raise Http404
	
	def get(self, request):
		question_id = request.GET.get("questionId")
		print "question"
		print question_id
		if question_id:
			question = get_object_or_404(Question, id=question_id)
			if question.user_name_id == request.user.id:
				question.delete()
				message = {"status": "success", "message":  "question deleted" }
			else:
				message = {"status": "error", "message":  "invalid user" }
		else:
			message = {"status": "error", "message":  "question id not found" }
			
		return http.HttpResponse(json.dumps(message), content_type="application/json")

	
class DeleteComment(View):
	print 'delete_comment'
	def get_object(self, id):
		try:
			return Comment.objects.get(id=id)
		except Comment.DoesNotExist:
			raise Http404
	
	def get(self, request):
		comment_id = request.GET.get("commentId")
		print "review"
		print comment_id
		if comment_id:
			comment = get_object_or_404(Comment, id=comment_id)
			if comment.user_id == request.user.id:
				comment.delete()
				message = {"status": "success", "message":  "comment deleted" }
			else:
				message = {"status": "error", "message":  "invalid user" }
		else:
			message = {"status": "error", "message":  "comment id not found" }
			
		return http.HttpResponse(json.dumps(message), content_type="application/json")

@login_required
def add_comment_to_review(request, destination_id, review_id):
	print "destination_id"
	review_id = request.GET.get("reviewId")
	destination_id = request.GET.get("destinationId")
	destination = get_object_or_404(Destination, pk=destination_id)
	if request.method =="GET":
		comment_form = CommentForm(request.GET)
		if request.GET.get('text'):
#	   if comment_form.is_valid():
#			text = comment_form.cleaned_data['text']
			comment = Comment()
			comment.text = request.GET.get('text')
#          comment.text = text
			comment.created_date = str(datetime.datetime.now())
			comment.review_id = review_id
			comment.user_id = request.user.id
			comment.save()
			data = {
				"datetime": comment.created_date,
				"username": request.user.username,
				"text": comment.text,
				"id": comment.id
			}
			message = {"status": "success", "message":  data }
		else:
			message = {"status": "error", "message":  "Please enter a comment."}
#	return redirect('destination_detail', slug=destination.slug)
	return http.HttpResponse(json.dumps(message), content_type="application/json")


@login_required
def add_comment_to_question(request, destination_id, question_id):
	print "destination_id"
	question_id = request.GET.get("questionId")
	destination_id = request.GET.get("destinationId")
	destination = get_object_or_404(Destination, pk=destination_id)
	if request.method =="GET":
		commentq_form = CommentQForm(request.GET)
		if request.GET.get('text'):
#	   if comment_form.is_valid():
#			text = comment_form.cleaned_data['text']
			commentq = CommentQ()
			commentq.text = request.GET.get('text')
#          comment.text = text
			commentq.created_date = str(datetime.datetime.now())
			commentq.question_id = question_id
			commentq.user_id = request.user.id
			commentq.save()
			data = {
				"datetime": commentq.created_date,
				"username": request.user.username,
				"text": commentq.text,
				"id": commentq.id
			}
			message = {"status": "success", "message":  data }
		else:
			message = {"status": "error", "message":  "Please enter a comment."}
#	return redirect('destination_detail', slug=destination.slug)
	return http.HttpResponse(json.dumps(message), content_type="application/json")


class DeleteCommentQ(View):
	print 'delete_commentq'
	def get_object(self, id):
		try:
			return CommentQ.objects.get(id=id)
		except CommentQ.DoesNotExist:
			raise Http404
	
	def get(self, request):
		commentq_id = request.GET.get("commentQId")
		print "review"
		print commentq_id
		if commentq_id:
			commentq = get_object_or_404(CommentQ, id=commentq_id)
			if commentq.user_id == request.user.id:
				commentq.delete()
				message = {"status": "success", "message":  "comment deleted" }
			else:
				message = {"status": "error", "message":  "invalid user" }
		else:
			message = {"status": "error", "message":  "comment id not found" }
			
		return http.HttpResponse(json.dumps(message), content_type="application/json")



