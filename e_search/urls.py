from django.urls import path
from . import views

urlpatterns = [
	path('seed', views.index),
	path('', views.PostListView.as_view()),
	path('e_search', views.PostDocumentView.as_view({'get': 'list'})),
	path('<int:pk>', views.PostDetailView.as_view()),
]
