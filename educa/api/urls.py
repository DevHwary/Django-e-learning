from django.urls import path
from . import views


urlpatterns = [

    path('courses/<pk>/enroll/',
         views.CourseEnrollView.as_view(),
         name='api_course_enroll'),


    # Subject
    path('subjects/',
         views.SubjectListView.as_view(),
         name='api_subject_list'),

    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='api_subject_detail'),



    # Course
    path('subjects/<pk>/courses/',
         views.CourseView.as_view(),
         name='api_course_list'),

    path('courses/<pk>/',
         views.CourseDetailView.as_view(),
         name='api_course_detail'),


    # Module
    path('course/<pk>/modules/',
         views.ModuleView.as_view(),
         name='api_module_list'),

    path('modules/<pk>/',
         views.ModuleDetailView.as_view(),
         name='api_module_detail'),

]
