from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task


class TaskViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='123'
        )

        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='pending',
            owner=self.user
        )

        self.client.login(username='testuser', password='123')

    def test_task_list_page(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_task_detail_page(self):
        response = self.client.get(f'/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)

