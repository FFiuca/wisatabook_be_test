from typing import Any
from django import forms

class PaginationField(forms.Field):
    def validate(self, value):
        if not isinstance(value, (dict, map)):
            raise forms.ValidationError("Invalid pagination value")
        if value.get('page') is None:
            raise forms.ValidationError("Page number is required")
        if value.get('limit') is None:
            raise forms.ValidationError("Limit number is required")

class ListField(forms.Field):
    def __init__(self, required=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.required = required

    def validate(self, value: Any) -> None:
        super().validate(value)
        if value is not None and not isinstance(value, list):
            raise forms.ValidationError("data_task_repeat must be array")
        if self.required and len(value) == 0:
            raise forms.ValidationError("data_task_repeat required")


class TaskForm(forms.Form):
    title =  forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=5000, required=False)
    data_task_repeat = ListField(required=False)
    due_date = forms.DateField(required=False)

class TaskListForm(forms.Form):
    title =  forms.CharField(max_length=100, required=False)
    status_id =  forms.IntegerField(required=False)
    pagination = PaginationField()
    # Making simple using PaginationField
    # def clean(self, value):
    #     super().clean()

    #     page = self.cleaned_data.get('page')
    #     limit = self.cleaned_data.get('page')

    #     if page is None and limit is not None:
    #         raise forms.ValidationError('Page must have value when Limit is set')

    #     return self.cleaned_data

class TaskChangeStatusForm(forms.Form):
    status_id =  forms.IntegerField(required=True)

class TaskChangeStarredStatusForm(forms.Form):
    starred_status =  forms.IntegerField(required=True)


