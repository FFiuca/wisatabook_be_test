import factory
from .. import models
from faker import Faker
from calendar import day_name

fake = Faker()

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Task

    title = factory.Sequence(lambda obj: fake.name())
    description = factory.LazyFunction(lambda: "\n".join(fake.paragraphs()))

class TaskRepeatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TaskRepeat

    task = factory.SubFactory(TaskFactory)
    day = factory.LazyFunction(lambda: fake.random_choices(elements=day_name, length=1)[0])
