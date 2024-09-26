from .. import models
from master import models as m_master
from . import service
from django.db import transaction
from . import serializer

class TaskUseCase:
    def __init__(
        self,
        svc_task = service.TaskService,
        svc_task_repeat = service.TaskRepeatService,
        status_model = m_master.Status,
        serializer = serializer.TaskSerializer
    ) -> None:
        self.svc_task = svc_task
        self.svc_task_repeat = svc_task_repeat
        self.status_model = status_model
        self.serializer = serializer

    def add(self, data):
        raise NotImplementedError("TaskUseCase not implented add method")

    def update(self, id, data):
        raise NotImplementedError("TaskUseCase not implented update method")

    def detail(self, id):
        raise NotImplementedError("TaskUseCase not implented detail method")

    def delete(self, id):
        raise NotImplementedError("TaskUseCase not implented delete method")

    def change_status(self, id, status_id):
        raise NotImplementedError("TaskUseCase not implented change_status method")

    def list(self, data, pagination):
        raise NotImplementedError("TaskUseCase not implented list method")

class TaskUseCaseImpl(TaskUseCase):

    # with db transaction
    @transaction.atomic
    def add(self, data:map, data_task_repeat=list):
        cls = self.svc_task()
        task = cls.add(data)

        cls = self.svc_task_repeat()
        task_repeat = cls.add(task, data_task_repeat)

        return task

    @transaction.atomic
    def update(self, id, data:map, data_task_repeat:list):
        cls = self.svc_task()
        task = cls.update(id, data)

        cls = self.svc_task_repeat()
        task_repeat = cls.add(task, data_task_repeat)

        return task

    @transaction.atomic
    def change_status(self, id, status_id):
        cls = self.svc_task()
        task = cls.change_status(id, status_id)

        return task

    @transaction.atomic
    def change_starred_status(self, id, starred_status):
        cls = self.svc_task()
        task = cls.change_starred_status(id, starred_status)

        return task

    def detail(self, id):
        cls = self.svc_task()
        task = cls.detail(id)

        serialize = self.serializer(task)
        # print(serialize.data)
        return serialize.data

    @transaction.atomic
    def delete(self, id):
        cls = self.svc_task()
        task = cls.delete(id)

        return task

    def list(self, param, pagination):
        cls = self.svc_task()
        data = cls.list(param, pagination)
        # print(data)
        data = self.serializer(data, many=True)
        # print(data.data)
        return data.data
