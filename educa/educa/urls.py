"""educa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cources.views import CourseListView

from django.conf import settings
from django.conf.urls.static import static

from schema_graph.views import Schema


urlpatterns = [

    path('admin/', admin.site.urls),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # instructor login
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),    # instructor logout

    path('course/', include('cources.urls')),  # courses app
    path('api/', include('api.urls')),  # API app

    path('', CourseListView.as_view(), name='course_list'),  # home page of courses

    path('students/', include('students.urls')),    # student app
    path('chat/', include('chat.urls', namespace='chat')),  # chat app

    path('schema/', Schema.as_view()),  # graph the schema of the models
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
