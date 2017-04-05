"""projectx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from collection import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='home'),
	url(r'^search/$', views.DestinationSearchView.as_view(), name='destination_search'),
	url(r'^destinations/(?P<slug>[-\w]+)/$', views.destination_detail, name='destination_detail'),
	url(r'^profiles/update/$', views.update_profile, name='update_profile'),
	url(r'^profiles/(?P<profile_id>[-\d]+)/$', views.profile_detail, name='profile_detail'),
	url(r'^municipalities/(?P<slug>[-\w]+)/$', views.muni_detail, name='muni_detail'),
	url(r'^provinces/(?P<slug>[-\w]+)/$', views.province_detail, name='province_detail'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^destinations/(?P<destination_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
	url(r'^destinations/(?P<destination_id>[0-9]+)/add_question/$', views.add_question, name='add_question'),
	url(r'^destinations/(?P<destination_id>[0-9]+)/add_comment_to_review/(?P<review_id>[0-9]+)$', views.add_comment_to_review, name='add_comment_to_review'),
	url(r'^destinations/(?P<destination_id>[0-9]+)/add_comment_to_question/(?P<question_id>[0-9]+)$', views.add_comment_to_question, name='add_comment_to_question'),
#	url(r'^profiles/edit_review/$', views.EditReview.as_view(), name='edit_review'),
	url(r'^profiles/delete_review/$', views.DeleteReview.as_view(), name='delete_review'),
	url(r'^profiles/delete_question/$', views.DeleteQuestion.as_view(), name='delete_question'),
	url(r'^profiles/delete_comment/$', views.DeleteComment.as_view(), name='delete_comment'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
