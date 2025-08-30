from django.contrib import admin
from .models import Subject, Teacher, Classroom, StudentGroup, TimetableEntry

# Simple registrations to make them appear in the admin panel
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(StudentGroup)

# A more customized admin view for Timetable Entries for better usability
@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = ('student_group', 'subject', 'teacher', 'day', 'time', 'classroom')
    list_filter = ('student_group', 'teacher', 'day')
    search_fields = ('subject__name', 'teacher__name', 'classroom__room_number')
    ordering = ('day', 'time')
