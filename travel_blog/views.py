from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = post
    template_name = 'article_details.html'