from xml.etree.ElementInclude import include
from django.urls import path, include

from devsearch.tags.views import CreateTagView, EditTagView,ListTagView,DeleteTagView

urlpatterns=[
    path('', ListTagView.as_view(), name='tags'),
    path('create/', CreateTagView.as_view(), name= 'tag create'),
    path('tag/<int:pk>/', include(
        [
            path('edit/', EditTagView.as_view(), name= 'tag edit'),
            path('delete/', DeleteTagView.as_view(), name='tag delete')
        ]
    ))
]