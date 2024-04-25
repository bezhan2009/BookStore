from django.urls import path
from . import views
# from .views import TaskList, TaskDetail, TaskDetailWithDetails, TaskView
# from .views import TaskView
from .views import BookView

urlpatterns = [
    path('books', BookView.as_view(), name='book-list'),
    # path('tasks/<int:task_id>/details', TaskView.as_view(), name='task-details'),
    # path('tasks/<int:task_id>', TaskView.as_view(), name='task-update-delete'),
]

# urlpatterns = [
#     path('', views.get_tasks),  # demo/api
#     path('create/', views.create_task),  # demo/api/create
#     path('update/<int:id>', views.update_task),  # demo/api/update
#     path('delete/<int:id>', views.soft_delete_task),  # demo/api/delete
#     path('get_by_id/<int:id>/details', views.get_task_by_id),  # demo/api/get_by_id
#
#     path('tasks/', TaskList.as_view(), name='task-list'),
#     path('tasks/<int:id>/', TaskDetail.as_view(), name='task-detail'),
#     path('tasks/<int:id>/details/', TaskDetailWithDetails.as_view(), name='task-detail-with-details'),
# ]

"""
[GET] /tasks
[POST] /tasks

[PUT] /tasks/<int:id>
[DELETE] /tasks/<int:id>

[GET] /tasks/<int:id>/details
"""
