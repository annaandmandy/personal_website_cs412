from django.shortcuts import render
# import class-based view template to use
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from django.urls import reverse_lazy # to redict through page name


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["on_profile_page"] = True
        return context
    
class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'mini_insta/become_friend.html'
    fields = ['username', 'display_name', 'profile_image_url', 'bio_text']
    success_url = reverse_lazy('profiles')

