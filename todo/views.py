from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, parsers
from rest_framework.response import Response
from rest_framework.decorators import action
from .src.forms import TaskForm, TaskListForm, TaskChangeStatusForm
from django.forms import ValidationError, model_to_dict
from .src.usecase import TaskUseCaseImpl

class TaskView(viewsets.ViewSet):
    parser_classes=[parsers.FormParser, parsers.JSONParser, parsers.MultiPartParser]

    def create(self, request, *args, **kwargs):
        data = request.data

        form = TaskForm(data=data)
        if form.is_valid() is False:
            raise ValidationError("Validation error")

        cls = TaskUseCaseImpl()
        add = cls.add({
            "title": form.cleaned_data['title'],
            "description": form.cleaned_data['description'],
        }, form.cleaned_data['data_task_repeat'])

        return Response(data={
            'status': 200,
            'data' : model_to_dict(add)
        }, status=200)

    def list(self, request):
        data = request.data

        form = TaskListForm(data=data)
        if form.is_valid() is False:
            raise ValidationError("Validation error")

        cls = TaskUseCaseImpl()
        data = cls.list({
            "title": form.cleaned_data['title'],
            "status_id": form.cleaned_data['status_id'],
        }, form.cleaned_data['pagination'])

        return Response(data={
            'status': 200,
            'data' : data
        }, status=200)

    def retrieve(self, request, pk=None):
        cls = TaskUseCaseImpl()
        data = cls.detail(pk)

        return Response(data={
            'status': 200,
            'data' : data
        }, status=200)

    def change_status(self, request, pk=None):
        data  = request.data
        # print(pk)
        form = TaskChangeStatusForm(data=data)
        if form.is_valid() is False:
            raise ValidationError("Validation error")

        cls = TaskUseCaseImpl()
        data = cls.change_status(pk, form.cleaned_data['status_id'])

        return Response(data={
            'status': 200,
            'data' : model_to_dict(data)
        }, status=200)

    def update(self, request, pk=None):
        data = request.data

        form = TaskForm(data=data)
        if form.is_valid() is False:
            raise ValidationError("Validation error")

        cls = TaskUseCaseImpl()
        add = cls.update(pk, {
            "title": form.cleaned_data['title'],
            "description": form.cleaned_data['description'],
        }, form.cleaned_data['data_task_repeat'])

        return Response(data={
            'status': 200,
            'data' : model_to_dict(add)
        }, status=200)

    def destroy(self, request, pk=None):
        cls = TaskUseCaseImpl()
        data = cls.delete(pk)

        return Response(data={
            'status': 200,
            'data' : data
        }, status=200)
