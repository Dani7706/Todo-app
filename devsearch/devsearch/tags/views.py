from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView, UpdateView
from devsearch.tags.models import Tag   


class ListTagView(ListView):
    model=Tag
    template_name='tags/tags.html'


class CreateTagView(CreateView):
    model=Tag
    template_name='tags/create-tag.html'
    success_url=reverse_lazy('tags')
    fields='__all__'

class EditTagView(UpdateView):
    model=Tag
    template_name='tags/edit-tag.html'
    success_url= reverse_lazy('tags')
    fields='__all__'



class DeleteTagView(DeleteView):
    model=Tag
    success_url=reverse_lazy('index')
    template_name='tags/delete-tag.html'
