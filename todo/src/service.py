from .. import models
from . import repositories
from typing import List
from django.db import models as m_django
from helpers.common_helper import paginate_model
from master import models as m_master

class TaskService(repositories.CRUDBase, repositories.ListBase):

    def __init__(
        self,
        task: m_django.Model= models.Task,
    ) -> None:
        self.task = task
        # self.task_repeat = task_repeat

    def add(self, data: map) -> m_django.Model :
        add = self.task.objects.create(**data)

        return add

    def update(self, id: int, data:map) -> m_django.Model:
        task = self.task.objects.get(pk=id)

        task.title = data['title']
        task.description = data['description']

        task.save()
        # update = self.task.objects.filter(id=id).update(**data)

        return task

    def detail(self, id: int) -> m_django.Model|None:
        data = self.task.objects.prefetch_related('task_to_task_repeat').select_related('status').filter(id=id).first()
        # print(data.task_to_task_repeat.all())
        return data

    def delete(self, id: int) -> any:
        delete = self.task.objects.filter(id=id).delete()

        return delete

    def change_status(self, id:int, status_id:int) -> m_django.Model:
        task = self.task.objects.get(pk=id)

        task.status = m_master.Status.objects.get(pk=status_id)
        task.save()

        return task

    def change_starred_status(self, id:int, starred_status:int) -> m_django.Model:
        task = self.task.objects.get(pk=id)

        task.starred_status = starred_status
        task.save()

        return task

    def list(self, param: map, pagination: map|None):
        q = self.task.objects.prefetch_related('task_to_task_repeat', 'status')
        if param.get('title') is not None:
            q = q.filter(title__contains=param['title'])
        if param.get('status_id') is not None:
            q = q.filter(status_id=param['status_id'])

        if pagination:
            page = paginate_model(pagination['page'], pagination['limit'])

            data = q.all()[page[0]:page[1]]
            # print(len(data))
            return data
        else:
            return q.all()


class TaskRepeatService(repositories.AddBase):

    def __init__(self, model: m_django.Model=models.TaskRepeat) -> None:
        self.model = model


    def add(self, task: models.TaskRepeat, data: list):
        # delete old first
        self.model.objects.filter(task=task).delete()

        # add again
        data = [
            self.model(
                task=task,
                day=i
            ) for i in data
        ]
        add = self.model.objects.bulk_create(data)

        return len(add)>0



