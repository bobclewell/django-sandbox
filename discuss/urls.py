from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.details, name='details'),
    url(r'^topic/new/$', views.new_topic, name='new_topic'),
    url(r'^topic/(?P<topic_id>[0-9]+)/comment/new/$', views.new_comment, name='new_comment'),
]