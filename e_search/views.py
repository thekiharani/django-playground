import json

import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework import generics
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend, \
	OrderingFilterBackend

from .documents import PostsDocument
from .models import Post
from .serializers import PostSerializer, PostDocumentSerializer


class PostListView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	serializer_class = PostSerializer


class PostDocumentView(DocumentViewSet):
	document = PostsDocument
	serializer_class = PostDocumentSerializer

	filter_backends = [
		FilteringFilterBackend,
		OrderingFilterBackend,
		CompoundSearchFilterBackend
	]

	search_fields = ('title', 'content')
	multi_match_search_fields = ('title', 'content')
	filter_fields = {
		'title': 'title',
		'content': 'content',
	}
	ordering_fields = {
		'id': None,
	}
	ordering = ('id',)


def generate_random_data():
	url = f"https://newsapi.org/v2/everything?q=Apple&from=2021-12-20&to=2021-12-20&sortBy=popularity&apiKey={settings.NEWS_API_KEY}"
	r = requests.get(url)
	payload = json.loads(r.text)
	# Post.objects.all().delete()
	count = 1
	for data in payload.get('articles'):
		print(count)

		Post.objects.create(
			title=data.get('title'),
			content=data.get('content'),
		)


def index(request):
	generate_random_data()
	return JsonResponse({'status': 200})
