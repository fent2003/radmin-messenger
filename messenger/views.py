from django.http import HttpResponse
from django.shortcuts import render
from messenger.utils import DataMixin
from django.views.generic import TemplateView

class Index(DataMixin, TemplateView):
    template_name = 'index.html'