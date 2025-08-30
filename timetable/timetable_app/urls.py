from django.urls import path
from . import views

# 

urlpatterns = [
    # Example URL: /timetables/group/1/
    # This will call the 'timetable_for_group' view with group_id=1
    path('group/<int:group_id>/', views.timetable_for_group, name='timetable_for_group'),
]
