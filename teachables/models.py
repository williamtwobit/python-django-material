from django.db import models

# Create your models here.
class Topic(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=140)

	def __str__(self):
		return self.title

class Lesson(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=140)
	intro = models.TextField()
	order = models.IntegerField(default=0)
	topic = models.ForeignKey(Topic)

	class Meta:
		ordering = ['order',]

	def __str__(self):
		return self.title

class Step(models.Model):
	title = models.CharField(max_length=50)
	order = models.IntegerField(default=0)
	lesson = models.ForeignKey(Lesson, default=1)
	content = models.TextField()
	image = models.ImageField(upload_to='user_uploaded/', default='placeholder.png')

	class Meta:
		ordering = ['order',]

	def __str__(self):
		return self.title