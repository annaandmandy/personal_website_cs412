from django.shortcuts import render
# import class-based view template to use
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = "object"
    slug_field = "username" # database column name
    slug_url_kwarg = "username" # url param name