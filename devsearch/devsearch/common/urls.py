from django.urls import path

from devsearch.common.views import index

urlpatterns=[
    path('', index, name='index'),
]