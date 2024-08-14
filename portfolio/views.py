from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from hitcount.views import HitCountDetailView
from .models import About,Contact,Service,Team,Client
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView
from django.core.paginator import Paginator


class AboutListView(ListView):
  model = About
  template_name = 'about.html'
  context_object_name = 'about'



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
      name = form.cleaned_data.get('name')
      phone_number = form.cleaned_data.get('phone_number')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {name}\nEmail: {email}\nPhone_number: {phone_number}\ntext: {content}"
      send_message(text)
      form.save()
      Contact.objects.create(
        name=name,
        phone_number=phone_number,
        email=email,
        content=content
    )
      return super().form_valid(form)






def home_view(request):
 return render(request=request,template_name='index.html')

class TeamListView(ListView):
  model = Team
  template_name = 'team.html'
  context_object_name = 'team'


class ServiceListView(ListView):
  model = Service
  template_name = 'service.html'
  context_object_name = 'service'



class ClientListView(ListView):
  model = Client
  paginate_by = 1
  template_name = 'client.html'
  context_object_name = 'client'

  def get_queryset(self):
        return Client.objects.all()
    