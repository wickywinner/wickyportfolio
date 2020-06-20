from django.contrib import admin
from django.urls import path, include
from home import views

# django admibn header customization
admin.site.site_header= "log in to WICKY Developer"
admin.site.site_title="Welcome to Wicky Dashboard"
admin.site.index_title="Welcome to this protal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('socialicon', views.socialicon, name='socialicon'),
]    