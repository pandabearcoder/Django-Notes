from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^edit/(?P<id>\d+)/$', views.Edit.as_view(), name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.Delete.as_view(), name='delete'),
    ]
