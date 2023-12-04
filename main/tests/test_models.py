from django.test import TestCase
from datetime import date, timedelta
from main.models import Task, Tag

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a tag for testing
        self.tag = Tag.objects.create(value='Test Tag')

    def test_create_task(self):
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            due_date=date.today() + timedelta(days=7),
            status='OPEN'
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.status, 'OPEN')

    def test_create_task_without_due_date(self):
        task = Task.objects.create(
            title='Task Without Due Date',
            description='This task has no due date.',
            status='OPEN'
        )
        self.assertIsNone(task.due_date)

    def test_create_task_with_tags(self):
        task = Task.objects.create(
            title='Task with Tags',
            description='This task has tags.',
            status='OPEN'
        )
        task.tags.add(self.tag)
        self.assertEqual(task.tags.count(), 1)
        self.assertEqual(task.tags.first(), self.tag)

    def test_task_string_representation(self):
        task = Task.objects.create(title='String Representation Test', description='Task for testing __str__ method')
        self.assertEqual(str(task), 'String Representation Test')

    def test_default_status_value(self):
        task = Task.objects.create(title='Default Status Test', description='Task for testing default status')
        self.assertEqual(task.status, 'OPEN')


class TagModelTest(TestCase):

    def test_create_tag(self):
        tag = Tag.objects.create(value='Test Tag')
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(tag.value, 'Test Tag')

    def test_tag_string_representation(self):
        tag = Tag.objects.create(value='String Representation Test')
        self.assertEqual(str(tag), 'String Representation Test')
