from django.shortcuts import render
from django.views.generic import ListView,DetailView


class ProjectsListView(ListView):
    template_name='projects/projects-list.html'

class ProjectDetailsView(DetailView):
    template_name='projects/single-project.html'

