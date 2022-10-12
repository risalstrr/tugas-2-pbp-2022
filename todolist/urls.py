from todolist.views import register
from django.urls import path
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import delete_todolist
from todolist.views import finished
from todolist.views import unfinished
from todolist.views import todolist_json
from todolist.views import create_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name="create-task"),
    path('delete-todolist/<int:id>/', delete_todolist, name="delete-todolist"),
    path('finished/<int:id>/',finished , name='finished'),
    path('unfinished/<int:id>/', unfinished, name='unfinished'),
    path('json/', todolist_json, name='todolist_json'),
    path('create-task-ajax/', create_task_ajax, name="create_task_ajax"),
]
