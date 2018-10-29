from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)
	imgpath = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Course(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	logo = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Branch(models.Model):
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')

ch = (
	(1,'EMAIL'),
	(2,'FACEBOOK'),
	(3,'PHONE'),
)

class Contact(models.Model):
	type = models.CharField(choices=ch, max_length=10, default=1)
	value = models.CharField(max_length=100)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
	def __str__(self):
		return self.type

