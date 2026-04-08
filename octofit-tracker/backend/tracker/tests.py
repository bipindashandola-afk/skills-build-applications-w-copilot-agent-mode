from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, Workout, User, Activity, Leaderboard

class APIRootTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class HealthCheckTest(APITestCase):
	def test_health_check(self):
		url = reverse('tracker-health')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

# Additional tests for CRUD endpoints can be added here
