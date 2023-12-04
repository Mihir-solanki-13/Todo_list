from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TagListCreateView, TagRetrieveUpdateDestroyView


class TestUrls(SimpleTestCase):
    
    def test_tasks_list_url(self):
        url = reverse('task-list-create')
        self.assertEqual(resolve(url).func.view_class , TaskListCreateView)

    def test_tags_list_url(self):
        url = reverse('tag-list-create')
        self.assertEqual(resolve(url).func.view_class , TagListCreateView)

    def test_task_update_delete_read(self):
        url = reverse('task-retrieve-update-destroy', args=['1'])
        self.assertEqual(resolve(url).func.view_class , TaskRetrieveUpdateDestroyView)

    def test_tag_update_delete_read(self):
        url = reverse('tag-retrieve-update-destroy', args=['1'])
        self.assertEqual(resolve(url).func.view_class , TagRetrieveUpdateDestroyView)
