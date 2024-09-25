from django.test import TestCase
from rest_framework.test import APITestCase
from todo.src.factories import TaskFactory, TaskRepeatFactory
from django.urls import reverse
from todo import models
import json

class UnitTest(APITestCase):
    fixtures = ['master']

    # def test_

class FeatureTest(APITestCase):
    fixtures = ['master']

    def setUp(self)->None:
        # super().setUp()

        self.task =  TaskFactory.create()
        self.task_repeat = TaskRepeatFactory.create_batch(3, task=self.task)

    def test_add(self):
        data = {
            "title" : self.task.title,
            "description" : self.task.description,
            "data_task_repeat" : [i.day for i in self.task_repeat]
        }
        # print(data)

        resp = self.client.post(reverse('todo:task-list'), data=json.dumps(data), content_type='application/json')
        # print(resp.json())

        task = models.Task.objects.filter(title=self.task.title).first()
        self.assertTrue(resp.status_code==200)
        self.assertTrue(task.title==self.task.title)
        self.assertTrue(len(task.task_to_task_repeat.all())>0)


    def test_detail(self):
        task = TaskFactory()
        task_repeat = TaskRepeatFactory.create_batch(3, task=task)

        resp = self.client.get(reverse('todo:task-detail', args=[task.pk]))
        # print(resp.json())

        self.assertTrue(resp.status_code==200)
        self.assertEqual(resp.json()['data']['id'], task.pk)

    def test_delete(self):
        task = TaskFactory.create()
        task_repeat = TaskRepeatFactory.create_batch(3, task=task)

        resp = self.client.delete(reverse('todo:task-detail', args=[task.pk]))
        # print(resp.json())

        task.refresh_from_db()
        self.assertTrue(resp.status_code==200)
        self.assertTrue(task.deleted is not None)

    def test_list(self):
        task = TaskFactory.create_batch(20)
        task_repeat = []
        for idx, val in enumerate(task):
            task_repeat.append(TaskRepeatFactory.create_batch(3, task=val))

        params = {
            'title' : 'a',
            'status_id':1,
            'pagination' : {
                'page': 2,
                'limit': 10
            }
        }

        resp = self.client.post(reverse('todo:task-list-post'),  data=json.dumps(params), content_type='application/json')

        # print(resp.json())

        self.assertTrue(resp.status_code==200)
        # self.assertEqual(resp.json()['data']['id'], task.pk)

    def test_update(self):
        new = TaskFactory()
        new_repeat = TaskRepeatFactory.create_batch(2, task=new)

        data = {
            "title" : new.title,
            "description" : new.description,
            "data_task_repeat" : [i.day for i in new_repeat]
        }
        # print(data)

        resp = self.client.put(reverse('todo:task-detail', args=[self.task.pk]), data=json.dumps(data), content_type='application/json')
        # print(resp.json())

        task = models.Task.objects.filter(title=new.title).first()
        self.assertTrue(resp.status_code==200)
        self.assertTrue(task.title==new.title)
        self.assertTrue(len(task.task_to_task_repeat.all())>0)




