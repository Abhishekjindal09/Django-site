from django.conf.urls import url

from . import views

urlpatterns = [
    #ex: /calendar/
    #url(r'', views.main, name='main'),
    #ex: /calendar/5/
    url(r'^(\d+)/$', views.main, name='main'),
]
