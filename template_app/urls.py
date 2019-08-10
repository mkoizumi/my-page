from django.conf.urls import url
from template_app import views

# app's own url
urlpatterns = [
    url(r'^model/$', views.model, name = 'model'),
    url(r'^help/$', views.help, name = 'help'),
]
