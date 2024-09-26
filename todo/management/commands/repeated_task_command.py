from django.core.management.base import BaseCommand
from todo.src.usecase import TaskUseCaseImpl

class Command(BaseCommand):
    help = 'Create repeated task'

    def handle(self, *args, **kwargs):
        self.stdout.write("Scheduled run")
        TaskUseCaseImpl().scheduler_repeated_task()
        self.stdout.write("Scheduled task completed")
