from rest_framework import serializers
from .. import models
from master.src.serialiezer import StatusSerializer

class TaskRepeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskRepeat
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'

    status = StatusSerializer(many=False, read_only=True)
    task_to_task_repeat = TaskRepeatSerializer(many=True, read_only=True)
