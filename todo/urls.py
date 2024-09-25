from django.urls import path, include
from .views import TaskView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', TaskView, basename='task')

app_name = 'todo'
urlpatterns = [
    path('', include(router.urls)),
    path('task/list', TaskView.as_view({'post': 'list'}), name='task-list-post'),
]

