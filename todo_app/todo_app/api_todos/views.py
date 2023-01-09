from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework import serializers, permissions, exceptions
from todo_app.api_todos.models import Todo, Category
from todo_app.api_todos.serializers import ListTodoSerializer, CreateTodoSerializer, CategorySerializer, \
    DetailTodoSerializer


class ListCreateTodoApiView(ListCreateAPIView):
    queryset = Todo.objects.all()
    list_serializer_class = ListTodoSerializer
    create_serializer_class = CreateTodoSerializer
    filter_name = ('category',)

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return self.__apply_filters_to_queryset(queryset)

    def __apply_filters_to_queryset(self, queryset):
        filter_params = {}
        for filter_name in self.filter_name:
            filter_id = self.request.query_params.get(filter_name, None)
            if filter_id:
                filter_params[filter_name] = filter_id
                queryset = queryset.filter(**filter_params)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class


class DetailTodoApiView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = DetailTodoSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        todo=super().get_object()
        if todo.user!=self.request.user:
            raise exceptions.PermissionDenied
        return todo


class ListCategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
