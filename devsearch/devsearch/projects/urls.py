from django.urls import path

from devsearch.projects.views import ProjectDetailsView, ProjectsListView

# from projects.views import ProjectDetailsView, ProjectsListView

urlpatterns=[
    path('', ProjectsListView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetailsView.as_view(), name='project detail'),
]