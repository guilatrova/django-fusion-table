from django.conf.urls import url
from locations import views

list_actions = {
    'get': 'list', 
    'post': 'create',
    'delete': 'destroy_all'
}

single_action = {
    'get': 'retrieve'
}

urlpatterns = [
    url(r'^$', views.LocationViewSet.as_view(list_actions), name='locations'),
    url(r'^(?P<pk>\d+)$', views.LocationViewSet.as_view(single_action), name='location')
]