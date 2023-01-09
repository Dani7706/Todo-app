from django.urls import path

from todo_app.api_todos.views import ListCreateTodoApiView, ListCategoryApiView, DetailTodoApiView

urlpatterns=[
    path('',ListCreateTodoApiView.as_view(), name='api list todos'),
    path('<int:pk>/',DetailTodoApiView.as_view(), name='api detail todo'),
    path('categories/', ListCategoryApiView.as_view(), name='api list categories'),
]