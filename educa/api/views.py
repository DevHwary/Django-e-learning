from rest_framework import generics
from cources.models import Subject, Course, Module
from . serializers import SubjectSerializer, CourseSerializer, ModuleSrializer, CourseWithContentsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEnrolled
from rest_framework.decorators import action
from rest_framework import viewsets


# So Important # # # # # # # # # #
class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})


# Subject
class SubjectListView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

#########################################################################


# Not prefered
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# course
class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):  # return courses of the subject
        self.subject = get_object_or_404(Subject, id=self.kwargs['pk'])
        return Course.objects.filter(subject=self.subject)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


#########################################################################


# module
class ModuleView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSrializer

    def get_queryset(self):
        self.course = get_object_or_404(Course, id=self.kwargs['pk'])
        return Module.objects.filter(course=self.course)


class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSrializer
