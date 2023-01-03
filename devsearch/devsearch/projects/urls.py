from xml.etree.ElementInclude import include
from django.urls import path, include

from devsearch.projects.views import ProjectDetailsView, ProjectsListView, ProjectCreateView, ProjectEditView, ProjectDeleteView

# from projects.views import ProjectDetailsView, ProjectsListView

urlpatterns=[
    path('', ProjectsListView.as_view(), name='projects'),
    path('add/', ProjectCreateView.as_view(), name='project create'),
    path('project/<int:pk>/', include(
        [
            path('', ProjectDetailsView.as_view(), name='project details'),
            path('edit/', ProjectEditView.as_view(), name='project edit'),
            path('delete/', ProjectDeleteView.as_view(), name='project delete')
        ]
    )),
]