#from django.urls import path
#from accounts.views import HomeView
#from accounts.views import AddView
from LMS import views
#from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django import template

urlpatterns = [
    # /LMS/ homepage
    #path('', HomeView.as_view(), name='home'),
    #path('', AddView.as_view(), name='add'),

    # /LMS/login/
   # path('login/', login, {'template_name': 'LMS/login.html'}),
]
