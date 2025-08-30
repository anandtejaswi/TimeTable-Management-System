from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    room_number = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField(default=30)

    def __str__(self):
        return self.room_number

class StudentGroup(models.Model):
    name = models.CharField(max_length=100, unique=True) # e.g., "Computer Science - Year 3"
    
    def __str__(self):
        return self.name

class TimetableEntry(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    
    TIME_CHOICES = [
        ('09:00 - 10:00', '09:00 - 10:00'),
        ('10:00 - 11:00', '10:00 - 11:00'),
        ('11:00 - 12:00', '11:00 - 12:00'),
        ('12:00 - 13:00', '12:00 - 13:00'),
        ('14:00 - 15:00', '14:00 - 15:00'),
        ('15:00 - 16:00', '15:00 - 16:00'),
        ('16:00 - 17:00', '16:00 - 17:00'),
    ]

    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    time = models.CharField(max_length=20, choices=TIME_CHOICES)

    class Meta:
        # Prevents booking conflicts
        unique_together = [('teacher', 'day', 'time'), ('classroom', 'day', 'time'), ('student_group', 'day', 'time')]
        verbose_name_plural = "Timetable Entries"

    def __str__(self):
        return f"{self.student_group} - {self.subject} on {self.day} at {self.time}"
