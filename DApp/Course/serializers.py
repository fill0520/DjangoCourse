from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Course, Contact, Category, Branch


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longtitude', 'address')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
	branches = BranchSerializer(many=True)
	contacts = ContactSerializer(many=True)
	category = serializers.StringRelatedField(many=False)

	class Meta:
		model = Course
		fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')
	
	def create(self, validated_data):
		course_br = validated_data.pop('branches')
		course_con = validated_data.pop('contacts')
		course = Course.objects.create(**validated_data, category=Category.objects.get(pk=1))
		for data in course_con:
			Contact.objects.create(contact=course, **data)
		for data in course_br:
			Branch.objects.create(branch=course, **data)
		return course
	