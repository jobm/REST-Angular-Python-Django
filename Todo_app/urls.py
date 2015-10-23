from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('',
    url(r'^todoitems/$', views.TodotList.as_view()),
    # url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
)
urlpatterns = format_suffix_patterns(urlpatterns)