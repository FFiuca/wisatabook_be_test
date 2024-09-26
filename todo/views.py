from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, parsers
from rest_framework.response import Response
from rest_framework.decorators import action
from .src.forms import TaskForm, TaskListForm, TaskChangeStatusForm, TaskChangeStarredStatusForm
from django.forms import ValidationError, model_to_dict
from .src.usecase import TaskUseCaseImpl
from helpers.common_helper import messageError

class TaskView(viewsets.ViewSet):
    parser_classes=[parsers.FormParser, parsers.JSONParser, parsers.MultiPartParser]

    def create(self, request, *args, **kwargs):
        data = request.data

        add=None
        form = None
        try:
            form = TaskForm(data=data)
            if form.is_valid() is False:
                raise ValidationError("Validation error")

            cls = TaskUseCaseImpl()
            add = cls.add({
                "title": form.cleaned_data['title'],
                "description": form.cleaned_data['description'],
                "due_date": form.cleaned_data['due_date']
            }, form.cleaned_data['data_task_repeat'])
        except ValidationError as e:
            return Response({'status':400, 'data': form.errors}, status=400)
        except  Exception as e:
            return Response({'status':500, 'data': messageError(e)}, status=500)

        return Response(data={
            'status': 200,
            'data' : model_to_dict(add)
        }, status=200)

    @action(methods=['post'], detail=False)
    def list_post(self, request):
        data = request.data

        form = None
        try:
            form = TaskListForm(data=data)
            if form.is_valid() is False:
                raise ValidationError("Validation error")

            cls = TaskUseCaseImpl()
            data = cls.list({
                "title": form.cleaned_data['title'],
                "status_id": form.cleaned_data['status_id'],
            }, form.cleaned_data['pagination'])
        except ValidationError as e:
            return Response({'status':400, 'data': form.errors}, status=400)
        except  Exception as e:
            return Response({'status':500, 'data': messageError(e)}, status=500)


        return Response(data={
            'status': 200,
            'data' : data
        }, status=200)

    def retrieve(self, request, pk=None):
        data = None
        try:
            cls = TaskUseCaseImpl()
            data = cls.detail(pk)
            # print(data)
        except  Exception as e:
            return Response({'status':500, 'data': messageError(e)}, status=500)

        return Response(data={
            'status': 200,
            'data' : data
        }, status=200)

    def change_status(self, request, pk=None):
        data  = request.data

        form=None
        try:
            form = TaskChangeStatusForm(data=data)
            if form.is_valid() is False:
                raise ValidationError("Validation error")

            cls = TaskUseCaseImpl()
            data = cls.change_status(pk, form.cleaned_data['status_id'])
        except ValidationError as e:
            return Response({'status':400, 'data': form.errors}, status=400)
        except  Exception as e:
            return Response({'status':500, 'data': messageError(e)}, status=500)

        return Response(data={
            'status': 200,
            'data' : model_to_dict(data)
        }, status=200)

    def change_starred_status(self, request, pk=None):
        data  = request.data

        form = None
        try:
            form = TaskChangeStarredStatusForm(data=data)
            if form.is_valid() is False:
                raise ValidationError("Validation error")

            cls = TaskUseCaseImpl()
            data = cls.change_starred_status(pk, form.cleaned_data['starred_status'])
        except ValidationError as e:
            return Response({'status':400, 'data': form.errors}, status=400)
        except  Exception as e:
            return Response({'status':500, 'data': messageError(e)}, status=500)

        return Response(data={
            'status': 200,
            'data' : model_to_dict(data)
        }, status=200)

    def update(self, request, pk=None):
        data = request.data

        update=None
        form=None
        try:
            form = TaskForm(data=data)
            if form.is_valid() is False:
                raise ValidationError("Validation error")

            cls = TaskUseCaseImpl()
            update = cls.update(pk, {
                "title": form.cleaned_data['title'],
                "description": form.cleaned_data['description'],
                "due_date": form.cleaned_data['due_date'],
            }, form.cleaned_data['data_task_repeat'])
        except ValidationError as e:
            return Response({'status':400, 'data': form.errors}, status=400)
        except  Exception as e:
            return Response({'status':500, 'data': messageError(e)}, status=500)

        return Response(data={
            'status': 200,
            'data' : model_to_dict(update)
        }, status=200)

    def destroy(self, request, pk=None):
        cls = TaskUseCaseImpl()
        data = cls.delete(pk)

        return Response(data={
            'status': 200,
            'data' : data
        }, status=200)
