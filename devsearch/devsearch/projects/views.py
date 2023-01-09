from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView

from devsearch.projects.models import Project
from devsearch.reviews.forms import ReviewForm
from devsearch.reviews.models import Review


class ProjectsListView(ListView):
    model=Project
    template_name='projects/projects-list.html'



        

class ProjectDetailsView(DetailView):
    model=Project
    template_name='projects/single-project.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        tags=self.object.tags.all()
        reviews=self.object.review_set.all()
        form=ReviewForm()
        context['tags']=tags
        context['reviews']=reviews
        context['form']=form
        return context

    # def post(self,request,*args,**kwargs):
    #     form=ReviewForm(request.POST)
    #     context= super().get_context_data(**kwargs)
    #     context['form']=form
    #     project=Project.objects.filter(pk=self.kwargs['pk']).get()
    #     if form.is_valid():
    #         value=form.cleaned_data['value']
    #         description= form.cleaned_data['description']
    #         review=Review.objects.create(
    #             value=value,description=description, project=project
    #         )
    #         review.save()
    #         form=ReviewForm()
    #         context['form']=form
    #         return self.render_to_response(context=context)
    #     return self.render_to_response(context=context)
class ProjectCreateView(CreateView):
    model=Project
    success_url=reverse_lazy('projects')
    fields=['title','description','demo_link', 'source_code','tags']
    template_name='projects/create-project.html'

class ProjectEditView(UpdateView):
    model=Project
    fields=['title','description','demo_link', 'source_code','tags']
    success_url=reverse_lazy('projects')
    template_name='projects/edit-project.html'

class ProjectDeleteView(DeleteView):
    model=Project
    success_url=reverse_lazy('index')
    template_name='projects/project-delete.html'


