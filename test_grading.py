import os
import django
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Assignment  # Adjust this according to your project structure

os.environ['DJANGO_SETTINGS_MODULE'] = 'fyleinterview.settings'
django.setup()

class GradingAPITestCase(APITestCase):
    def setUp(self):
        # Create test data for assignments
        self.assignment = Assignment.objects.create(content="Test assignment", state="SUBMITTED", student_id=1, teacher_id=1)
    
    def test_grade_assignment(self):
        url = reverse('regrade_assignment')
        data = {"id": self.assignment.id, "grade": "A"}
        headers = {"HTTP_X_Principal": '{"user_id":5, "principal_id":1}'}
        
        response = self.client.post(url, data, **headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['grade'], 'A')
    
    def test_regrade_assignment(self):
        # First, grade the assignment
        self.assignment.grade = "B"
        self.assignment.state = "GRADED"
        self.assignment.save()

        url = reverse('regrade_assignment')
        data = {"id": self.assignment.id, "grade": "A"}
        headers = {"HTTP_X_Principal": '{"user_id":5, "principal_id":1}'}

        response = self.client.post(url, data, **headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['grade'], 'A')
