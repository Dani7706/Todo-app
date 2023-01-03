from devsearch.reviews.views import create_review
from django.urls import path

urlpatterns=[
    path('add/<int:project_pk>', create_review, name ='review add'),
]