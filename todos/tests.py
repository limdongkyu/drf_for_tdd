import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import TodoSerializer
from .models import Todo


class TodoModelTest(APITestCase):
    """
    모델 검증
    """
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='model_tester', email='model_tester@test.com')
        cls.todo = Todo.objects.create(user=cls.user, name='todo title')
        
    def test_user_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('user').verbose_name
        self.assertEquals(field_label, '작성자')
    
    def test_name_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('name').verbose_name
        self.assertEquals(field_label, '제목')
    
    def test_done_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('done').verbose_name
        self.assertEquals(field_label, '성공여부')

    def test_date_created_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('date_created').verbose_name
        self.assertEquals(field_label, '생성날짜')
    
    def test_name_max_length(self):
        todo = Todo.objects.get(id=1)
        max_length = todo._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
    
    def test_todo_str(self):
        self.assertTrue(isinstance(self.todo, Todo))
        self.assertEquals(self.todo.__str__(), self.todo.name)


class TodoListCreateAPIViewTestCase(APITestCase):
    """
    Todo 생성 및 리스트
    """
    url = reverse('todos:list')

    def setUp(self):
        self.username = 'tester'
        self.email = 'tester@test.com'
        self.password = 'abcede00**'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_todo(self):
        """
        생성
        """
        response = self.client.post(self.url, {'name': '샘플2 만들기'})
        self.assertEqual(201, response.status_code)

    def test_user_todos(self):
        """
        리스트 갯수
        """
        Todo.objects.create(user=self.user, name='샘플JWT 만들기')
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Todo.objects.count())


class TodoDetailAPIViewTestCase(APITestCase):
    """
       Todo-CRUD
    """
    def setUp(self):
        self.username = 'tester'
        self.email = 'tester@test.com'
        self.password = 'abcede00**'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.todo = Todo.objects.create(user=self.user, name='샘플2 만들기')
        self.url = reverse('todos:detail', kwargs={'pk': self.todo.pk})
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_todo_object_bundle(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        todo_serializer_data = TodoSerializer(instance=self.todo).data
        response_data = json.loads(response.content)
        self.assertEqual(todo_serializer_data, response_data)

    def test_todo_object_update_authorization(self):
        new_user = User.objects.create_user('tester2', 'tester2@test.com', 'abcede00**')
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)

        # PUT all data
        response = self.client.put(self.url, {'name': '바뀌면 안되는데...', 'done': True})
        self.assertEqual(403, response.status_code)

        # PATCH
        response = self.client.patch(self.url, {'name': '바뀌면 안되는데...'})
        self.assertEqual(403, response.status_code)

    def test_todo_object_update(self):
        response = self.client.put(self.url, {'name': '이직하기 ㅋㅋㅋ'})
        response_data = json.loads(response.content)
        todo = Todo.objects.get(id=self.todo.id)
        self.assertEqual(response_data.get('name'), todo.name)

    def test_todo_object_partial_update(self):
        response = self.client.patch(self.url, {'done': True})
        response_data = json.loads(response.content)
        todo = Todo.objects.get(id=self.todo.id)
        self.assertEqual(response_data.get('done'), todo.done)

    def test_todo_object_delete_authorization(self):
        new_user = User.objects.create_user('tester2', 'tester2@test.com', 'abcede00**')
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)

    def test_todo_object_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
