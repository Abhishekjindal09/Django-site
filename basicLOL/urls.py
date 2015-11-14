from django.conf.urls import url

from . import views

urlpatterns = [
    #ex: /basicLOL/summoner/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
