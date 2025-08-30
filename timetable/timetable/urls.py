"""
URL configuration for timetable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# This is the main URL configuration for the entire project.
# It directs traffic to the appropriate app.

urlpatterns = [
    # The built-in Django admin site
    path('admin/', admin.site.urls),
    
    # This line includes all the URLs from your 'timetable_app'
    # Any URL starting with 'timetables/' will be handled by timetable_app/urls.py
    path('timetables/', include('timetable_app.urls')),
]
