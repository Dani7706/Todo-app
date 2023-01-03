from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy

from devsearch.projects.models import Project
from devsearch.reviews.models import Review
from devsearch.reviews.forms import ReviewForm

# class CreateReviewView(CreateView):
#     model= Review
#     # template_name='reviews/create-review.html'
#     template_name = 'projects/single-project.html'
#     fields = ['description', 'value']
#     success_url = reverse_lazy('index')
#
#     # def get_context_data(self, **kwargs):
#     #     context= super(CreateReviewView, self).get_context_data()
#     #     context['project_pk']=self.object.project.pk
#     #     return context
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         project=Project.objects.filter(pk=self.object.project_id).get()
#         form.instance.project=project
#         return super(CreateReviewView, self).form_valid()

def create_review(request, project_pk):
    project=Project.objects.filter(pk=project_pk).get()
    form = ReviewForm(request.POST)
    if form.is_valid():
        review= form.save(commit=False)
        review.project=project
        review.save()
    return redirect('project details', pk=project_pk)