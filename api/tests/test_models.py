from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Task , Tag

import datetime

class TestTask(TestCase):

    def setUp(self):
        self.user_model = get_user_model()
        self.random_user = self.user_model.objects.create(
            username = 'chegreyev' ,
            password = '1601'
        )


        self.random_task = Task.objects.create(
            user = self.random_user ,
            name = 'random task' ,
            description = 'Just a random description',
            creation_date = datetime.date.today()
        )

    def test_test_name_is_correct(self):
        self.assertEqual(self.random_task.name , 'random task')

class TestTag(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.random_user = self.user_model.objects.create(
            username='chegreyev',
            password='1601'
        )

        self.random_task = Task.objects.create(
            user=self.random_user,
            name='random task',
            description='Just a random description',
            creation_date=datetime.date.today()
        )

        self.random_tag = Tag.objects.create(
            task = self.random_task ,
            name = 'tag name' ,
            creation_date = datetime.date.today()
        )

    def test_test_name_is_correct(self):
        self.assertEqual(self.random_tag.name, 'tag name')