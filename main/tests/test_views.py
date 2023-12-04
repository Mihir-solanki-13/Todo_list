# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Task, Tag
from main.serializers import TaskSerializer, TagSerializer
from django.test import TestCase


class TaskViewsTest(APITestCase):

    def setUp(self):
        # Create some test data
        self.task_data = {'title': 'Test Task', 'description': 'Test Description', 'status': 'OPEN'}
        self.task = Task.objects.create(**self.task_data)
        

        # Define URLs for Task views
        self.task_list_create_url = reverse('task-list-create')
        self.task_detail_url = reverse('task-retrieve-update-destroy', args=[self.task.id])
        # print('tasks:',self.task_list_create_url)
    def test_task_list_create_view(self):
        response = self.client.get(self.task_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test creating a new task
        response = self.client.post(self.task_list_create_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_retrieve_update_destroy_view(self):
        # Test retrieving a task
        response = self.client.get(self.task_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test updating a task
        # updated_data = {'title': 'Updated Task', 'description': 'Updated Description', 'status': 'DONE'}
        # response = self.client.put(self.task_detail_url, updated_data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['title'], 'Updated Task')
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description', 'status': 'DONE'}
        response = self.client.put(self.task_detail_url, updated_data, format='json')
        # print(f"url: {self.task_detail_url}")
        # print(f"Response data: {response.data}")
        # print(f"Response status code: {response.status_code}")
        # print(f"Response data: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')


        # Test deleting a task
        response = self.client.delete(self.task_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

class TagViewsTest(TestCase):
    def setUp(self):
        # Clear the database before each test
        Tag.objects.all().delete()

class TagViewsTest(APITestCase):

    def setUp(self):
        # Create some test data
        self.tag_data = {'value': 'T'}
        self.tag = Tag.objects.create(**self.tag_data)

        # Define URLs for Tag views
        self.tag_list_create_url = reverse('tag-list-create')
        self.tag_detail_url = reverse('tag-retrieve-update-destroy', args=[self.tag.id])

    def test_tag_list_create_view(self):
    # Test retrieving the tag list
        response = self.client.get(self.tag_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test creating a new tag
        print(f"url: {self.tag_list_create_url}")
        print(f"data: {self.tag_data}")

        # Update the tag_data to use a unique value
        unique_tag_data = {'value': 'UniqueTag'}
        response = self.client.post(self.tag_list_create_url, unique_tag_data, format='json')

        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tag_retrieve_update_destroy_view(self):
        # Test retrieving a tag
        response = self.client.get(self.tag_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test updating a tag
        updated_data = {'value': 'Updated Tag'}
        response = self.client.put(self.tag_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['value'], 'Updated Tag')

        # Test deleting a tag
        response = self.client.delete(self.tag_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
