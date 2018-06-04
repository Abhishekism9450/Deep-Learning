from django.conf.urls import url
from easytorch import views

urlpatterns=[
    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
]
