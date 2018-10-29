from rest_framework import serializers
from Course.models import Course, Contact, Category, Branch


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')

class CourseSerializerPOST(serializers.ModelSerializer):
    
	branches = BranchSerializer(many=True)
	contacts = ContactSerializer(many=True)

	class Meta:
		model = Course
		fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')
	
	def create(self, validated_data):
		course_br = validated_data.pop('branches')
		course_con = validated_data.pop('contacts')

		course = Course.objects.create(**validated_data)
		for data in course_con:
			Contact.objects.create(course=course, **data)
		for data in course_br:
			Branch.objects.create(course=course, **data)
		return course

class CourseSerializerGET(serializers.ModelSerializer):
    
	branches = BranchSerializer(many=True)
	contacts = ContactSerializer(many=True)
	category = serializers.StringRelatedField(many=False)

	class Meta:
		model = Course
		fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')


		