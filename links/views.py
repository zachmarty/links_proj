from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DeleteView
from links.models import Link
from django.urls import reverse_lazy
from links.forms import LinkForm
import hashlib

class LinksIndex(CreateView):
    model = Link
    form_class = LinkForm
    success_url = reverse_lazy('user:profile')
    template_name = 'links/base.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        new_link = form.save()
        print(self.request.user)
        url_bytes = new_link.link.encode('utf-8')
        hash_bytes = hashlib.sha256(url_bytes).digest()
        hash_str = hash_bytes.hex()
        short_url = hash_str[:8]
        new_link.hash_code = short_url
        new_link.save()
        return super().form_valid(form)
    
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy("user:profile")
    template_name = 'links/link_confirm_delete.html'