from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fashion/$', views.fashion, name='fashions'),
    url(r'^like/$', views.like, name='like'),
    url(r'^beauty/$', views.beauty, name='beauty'),
    url(r'^lifestyle/$', views.lifestyle, name='lifestyle'),
    url(r'^travel/$', views.travel, name='travel'),
    url(r'^fitness/$', views.fitness, name='fitness'),
    url(r'^post/(?P<pk>\d+)/$', views.show_post, name='show_post'),
    url(r'^comment/(?P<pk>\d+)/$', views.comment, name='comment'),
]
