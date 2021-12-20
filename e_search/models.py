from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(max_length=10000)
	date_created = models.DateTimeField(auto_now_add=True, blank=True)
	last_updated = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'e_search_posts'
