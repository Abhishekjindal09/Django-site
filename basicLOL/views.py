from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Summoner

# Create your views here.

class DetailView(generic.DetailView):
    model = Summoner
    template_name = 'summoner/detail.html'
