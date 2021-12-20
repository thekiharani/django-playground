from django_elasticsearch_dsl import Document, fields, Index

from .models import Post

PUBLISHER_INDEX = Index('elastic_demo')
PUBLISHER_INDEX.settings(
	number_of_shards=1,
	number_of_replicas=1
)


@PUBLISHER_INDEX.doc_type
class PostsDocument(Document):
	id = fields.IntegerField(attr='id')
	title = fields.TextField(
		fields={
			"raw": {
				"type": "keyword"
			}
		}
	)
	content = fields.TextField(
		fields={
			"raw": {
				"type": "keyword"
			}
		}
	)
	date_created = fields.DateField(attr='date_created')
	last_updated = fields.DateField(attr='last_updated')

	class Django(object):
		model = Post
