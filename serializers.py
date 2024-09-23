from rest_framework import serializers
from .models import Assignment, Teacher

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'content', 'created_at', 'grade', 'state', 'student_id', 'teacher_id', 'updated_at']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user_id', 'created_at', 'updated_at']
