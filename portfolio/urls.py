from django.urls import path
from .views import home_view, AboutListView,ServiceListView,ClientListView,ContactFormView,TeamListView


urlpatterns = [
    path('',home_view,name='index-page'),
    path('about/',AboutListView.as_view(),name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('service/',ServiceListView.as_view(),name='service-page') ,
    path('team/',TeamListView.as_view(),name='team-page'),
    path('client/',ClientListView.as_view(),name='client-page' )


]