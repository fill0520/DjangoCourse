from django.test import TestCase
from .models import Course, Contact, Category, Branch
# Create your tests here.

class CategoryModelTest(TestCase):
	def create_category(name='new', imgpath='root'):
		return Category.objects.create(name=name, imgpath=imgpath)
	def test_create_category(self):
		category = self.create_category()
		self.assertEqual(category.__str__(), category.name)
		self.assertTrue(isinstance(category, Category))



class CourseModelTest(TestCase):
	def create_course(self):
		course = Course.objects.create(
				name='test_cases',
				description='test_cases',
				logo='test_cases',
				category=CategoryModelTest.create_category()
			)
		return course

	def test_create_course_1(self):
		c = self.create_course()
		c.contacts.create(
			type='EMAIL',
			value='root@roor.com'
		)
		c.branches.create(
			latitude='test_cases',
			longtitude='test_cases',
			address='test_cases'
		)
		self.assertTrue(isinstance(c, Course))
		self.assertEqual(c.contacts.get(pk=1).type, 'EMAIL')

	def test_create_course_2(self):
		c = self.create_course()
		c.contacts.create(
			type='EMAIL',
			value='root@roor.com'
		)
		c.contacts.create(
			type='FACEBOOK',
			value='face'
		)
		c.branches.create(
			latitude='test_cases',
			longtitude='test_cases',
			address='test_cases'
		)
		self.assertEqual(c.contacts.get(pk=1).value, 'root@roor.com')
		self.assertEqual(c.contacts.get(pk=2).type, 'FACEBOOK')
		self.assertEqual(c.branches.get(pk=1).address, 'test_cases')
