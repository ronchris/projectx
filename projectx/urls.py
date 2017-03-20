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
	url(r'^munis/(?P<slug>[-\w]+)/$', views.muni_detail, name='muni_detail'),
	url(r'^provinces/(?P<slug>[-\w]+)/$', views.province_detail, name='province_detail'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	url(r'^destinations/(?P<destination_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
