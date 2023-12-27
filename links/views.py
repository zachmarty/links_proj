from typing import Any
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, TemplateView
from links.models import Link
from django.urls import reverse_lazy
from links.forms import LinkForm
from django.shortcuts import get_object_or_404, render
import hashlib
from django.utils import timezone

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
    template_name = 'links/link_confirm_delete.html'
    success_url = reverse_lazy("user:profile")
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        obj = get_object_or_404(Link, id = self.object.pk, user = request.user.id)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
def link_redirect(request, code):
    link = Link.objects.get(hash_code = code)
    link.last_click = timezone.now()
    link.save()
    return HttpResponseRedirect(link.link)
        