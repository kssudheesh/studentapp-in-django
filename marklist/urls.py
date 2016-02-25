from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^new/$', views.new, name="new"),
	url(r'^(?P<student_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^(?P<student_id>[0-9]+)/delete$', views.delete, name="delete"),
	url(r'^(?P<student_id>[0-9]+)/edit$', views.edit, name="edit"),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^search/$', views.search, name='search'),
]