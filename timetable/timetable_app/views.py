from django.shortcuts import render, get_object_or_404
from .models import TimetableEntry, StudentGroup

def timetable_for_group(request, group_id):
    """
    Displays the timetable for a specific student group, organized in a grid.
    This view prepares the data in a list-of-lists format so the template can
    easily render it without complex logic.
    """
    student_group = get_object_or_404(StudentGroup, id=group_id)
    all_entries = TimetableEntry.objects.filter(student_group=student_group)

    # Use choices from the model to ensure a consistent and full order
    days = [day[0] for day in TimetableEntry.DAY_CHOICES]
    times = [time[0] for time in TimetableEntry.TIME_CHOICES]

    # Create a lookup dictionary for fast access to existing entries
    entry_map = { (entry.day, entry.time): entry for entry in all_entries }

    # Build the grid structure for the template. This list of rows will contain cells.
    schedule_grid = []
    for time in times:
        row = {'time': time, 'entries': []}
        for day in days:
            # Get the entry from our map, or None if no class is scheduled
            entry = entry_map.get((day, time))
            row['entries'].append(entry)
        schedule_grid.append(row)

    context = {
        'student_group': student_group,
        'schedule_grid': schedule_grid,
        'days': days,
    }
    return render(request, 'timetable_app/timetable_detail.html', context)
