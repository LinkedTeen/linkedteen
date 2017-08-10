from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]

#<a href="{% url 'index' %}">Home</a>.
