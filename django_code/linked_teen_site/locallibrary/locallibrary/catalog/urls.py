from django.conf.urls import url

from . import views

urlpatterns += [   
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

#<a href="{% url 'index' %}">Home</a>.
