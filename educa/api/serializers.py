from rest_framework import serializers
from cources.models import Subject, Course, Module, Content


# Items of content
class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)

    class Meta():
        model = Content
        fields = ['order', 'item']
###########################################


class SubjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleForCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'course']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleForCourseSerializer(many=True, read_only=True)
    subject_title = serializers.StringRelatedField(source='subject.title')

    class Meta():
        model = Course
        fields = ['id', 'subject', 'subject_title', 'title', 'slug', 'overview', 'created', 'owner', 'modules']


######
'''
class CourseForModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']
'''


class ModuleSrializer(serializers.ModelSerializer):
    course_name = serializers.StringRelatedField(source='course.title')

    class Meta:
        model = Module
        fields = ['course', 'course_name', 'order', 'title', 'description']
