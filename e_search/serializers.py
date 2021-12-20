from rest_framework.serializers import ModelSerializer
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import Post
from .documents import PostsDocument


class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'pk', 'title', 'content', 'date_created', 'last_updated',
		]
		extra_kwargs = {
			'date_created': {'required': False},
			'last_updated': {'required': False},
		}


class PostDocumentSerializer(DocumentSerializer):
	class Meta:
		model = Post
		document = PostsDocument

		fields = [
			'id', 'title', 'content', 'date_created', 'last_updated',
		]

		def get_location(self, obj):
			try:
				return obj.location.to_dict()
			except:
				return {}
