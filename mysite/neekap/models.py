from django.db import models
from django.db.models import permalink
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

# Create your models here.

class Logo(models.Model):
	picture = models.ImageField(upload_to='art', default='blog1.png')

class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	picture = models.ImageField(upload_to='art', default='images/blog/1.png')
	# slug is the unique url
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('neekap.Category', on_delete=models.CASCADE)
	document = models.FileField(upload_to='art', default='1.png')
	content = HTMLField(default='none')

	def __str__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug })


class trial(models.Model):
	content = RichTextField()
	contents = RichTextField(default='none')
class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	# How to create a basic blog in django
	def __str__(self):
		return '%s' % self.title

	# /blog/view/how-to-create-a-basic-blog-in-django.html
	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug})

class SlideShow(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	bubble = models.CharField(max_length=50, db_index=True, default='')
	slug = models.SlugField(max_length=100, db_index=True, default='')

	def __str__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug})

# Mission of the website
# class Mission(models.Model):
# 	title = models.CharField(max_length=100, db_index=True, default='')
# 	statement = models.TextField(default='')

# 	def __str__(self):
# 		return '%s' % self.title

class StatsFactor(models.Model):
	image = models.ImageField(upload_to='', default='art')
	text = models.CharField(max_length=100, db_index=True)
