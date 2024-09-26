from django.urls import path, include
from .views import TaskView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', TaskView, basename='task')

app_name = 'todo'
urlpatterns = [
    path('', include(router.urls)),
    # path('task/list/', TaskView.as_view({'post': 'list_post'}), name='task-list-post'),
    path('task/<int:pk>/change_status/', TaskView.as_view({'patch': 'change_status'}), name='task-change-status'),
    path('task/<int:pk>/change_starred_status/', TaskView.as_view({'patch': 'change_starred_status'}), name='task-change-starred-status'),
]

