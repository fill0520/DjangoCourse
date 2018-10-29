from django.contrib import admin

from .models import Course, Contact, Category, Branch
# Register your models here.

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class BranchInline(admin.TabularInline):
    model = Branch
    extra = 1

class CourseAdmin(admin.ModelAdmin):  
    inlines = [ContactInline, BranchInline] 


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)

