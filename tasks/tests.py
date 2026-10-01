from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Project,Task
class TaskFlowTests(TestCase):
 def setUp(self):
  self.user=User.objects.create_user("leo",password="test12345");self.project=Project.objects.create(name="Teste",owner=self.user)
 def test_login_required(self):self.assertEqual(self.client.get(reverse("dashboard")).status_code,302)
 def test_dashboard(self):
  self.client.login(username="leo",password="test12345");self.assertEqual(self.client.get(reverse("dashboard")).status_code,200)
 def test_task(self):
  Task.objects.create(project=self.project,title="Tarefa");self.assertEqual(Task.objects.count(),1)