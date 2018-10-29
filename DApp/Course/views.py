from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Course.serializers import CourseSerializerPOST, CourseSerializerGET
from Course.models import Course, Contact, Category, Branch

class CourseViewSet(viewsets.ModelViewSet):
    
    queryset = Course.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CourseSerializerPOST
        return CourseSerializerGET
    

