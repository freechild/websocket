from django.conf.urls import url
from . import views
 
app_name = "websocketApp"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^create/$', views.create, name='create'),
    # url(r'^show/$', views.show, name='show'),
    # url(r'^delete/(?P<document_id>[a-z0-9]*)/$', views.delete, name='delete'),
]