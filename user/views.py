from django.db.models.base import Model as Model
from django.shortcuts import HttpResponseRedirect
from user.models import User
from django.views.generic import CreateView, UpdateView
from user.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from links.models import Link

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')
    
    
class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('links:index')
    template_name = 'user/profile.html'
    
    def get_object(self, queryset = None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        links = Link.objects.filter(user = self.request.user)
        context['links'] = links
        return context
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('links:index'))