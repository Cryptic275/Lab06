from django.db import models


class Course(models.Model):
    id = models.CharField(max_length=6, primary_key=True, name="courseID")
    name = models.CharField(max_length=128, name="courseName")

    def __unicode__(self):
        return '%s %s' % (self.courseID, self.courseName)

    def __str__(self):
        return '%s - %s' % (self.courseID, self.courseName)

class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True, name="studentID")
    name = models.CharField(max_length=128, name="studentName")
    gpa = models.FloatField()
    courses = models.ManyToManyField(Course, blank=True, related_name='students')

    def __unicode__(self):
        return self.studentName

    def __str__(self):
        return self.studentName