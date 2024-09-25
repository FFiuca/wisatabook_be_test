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
        super().setUp()

        self.task =  TaskFactory.create()
        self.task_repeat = TaskRepeatFactory.create_batch(3, task=self.task)

    # This test case verifies the addition of a task by sending a POST request to the task-list endpoint,
    # checking that the response status is 200, and confirming that the task was created in the database
    # with the expected title and associated task repeats.
    def test_add(self):
        data = {
            "title": self.task.title,
            "description": self.task.description,
            "data_task_repeat": [i.day for i in self.task_repeat]
        }

        resp = self.client.post(reverse('todo:task-list'), data=json.dumps(data), content_type='application/json')

        task = models.Task.objects.filter(title=self.task.title).first()
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(task.title == self.task.title)
        self.assertTrue(len(task.task_to_task_repeat.all()) > 0)


    # This test case verifies the detail view of a task. It creates a task and a batch of task repeats,
    # then sends a GET request to the task detail endpoint. It checks that the response status code is 200
    # and that the returned task ID matches the created task's primary key.
    def test_detail(self):
        task = TaskFactory()
        task_repeat = TaskRepeatFactory.create_batch(3, task=task)

        resp = self.client.get(reverse('todo:task-detail', args=[task.pk]))

        self.assertTrue(resp.status_code==200)
        self.assertEqual(resp.json()['data']['id'], task.pk)

    # This test case verifies the deletion of a task in the to-do application.
    # It creates a task and a batch of repeating tasks, then sends a DELETE request to
    # remove the task. After the request, it checks that the response status code is 200
    # and confirms that the task has been marked as deleted in the database.
    def test_delete(self):
        task = TaskFactory.create()
        task_repeat = TaskRepeatFactory.create_batch(3, task=task)

        resp = self.client.delete(reverse('todo:task-detail', args=[task.pk]))

        task.refresh_from_db()
        self.assertTrue(resp.status_code==200)
        self.assertTrue(task.deleted is not None)

    # This test case checks the functionality of changing the status of a task.
    # It creates a task and a batch of task repeats, then sends a PATCH request
    # to update the task's status. After the request, it verifies that the
    # response status code is 200 and that the task's status has been updated
    # correctly in the database.
    def test_change_status(self):
        task = TaskFactory.create()
        task_repeat = TaskRepeatFactory.create_batch(3, task=task)

        data = {
            'status_id': 2
        }

        resp = self.client.patch(reverse('todo:task-change-status', args=[task.pk]), data=json.dumps(data),  content_type='application/json')

        task.refresh_from_db()
        self.assertTrue(resp.status_code==200)
        self.assertTrue(task.status_id==data['status_id'])

    # This test case verifies the functionality of creating tasks and their repetitions. It creates a batch of tasks and associated task repetitions, then sends a POST request to the task list endpoint with pagination parameters. Finally, it checks that the response status is 200 and that there are tasks in the response data.
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

        self.assertTrue(resp.status_code==200)
        self.assertTrue(len(resp.json()['data'])>0)

    # This test case verifies the update functionality of a task in the to-do application.
    # It creates a new task and a batch of task repeats, prepares a data dictionary with the task details,
    # and sends a PUT request to update the task. Finally, it checks if the response status is 200,
    # confirms that the task title remains unchanged, and ensures that the task has associated repeats.
    def test_update(self):
        new = TaskFactory()
        new_repeat = TaskRepeatFactory.create_batch(2, task=new)

        data = {
            "title" : new.title,
            "description" : new.description,
            "data_task_repeat" : [i.day for i in new_repeat]
        }

        resp = self.client.put(reverse('todo:task-detail', args=[self.task.pk]), data=json.dumps(data), content_type='application/json')

        task = models.Task.objects.filter(title=new.title).first()
        self.assertTrue(resp.status_code==200)
        self.assertTrue(task.title==new.title)
        self.assertTrue(len(task.task_to_task_repeat.all())>0)




