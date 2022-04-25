from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='First Todo', body='The first todo')
        Todo.objects.create(title='Second Todo', body='The second todo')

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'First Todo')
    
    def test_todo_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'The first todo')
    