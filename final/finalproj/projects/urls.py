from . import views
from django.urls import path

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('sort/<sort_by>', views.index_sorted, name='index_sorted'),
    path('<int:project_id>', views.detail, name='detail'),
    path('add', views.create_project, name='create_project'),
    path('update/<int:id>', views.update_project, name='update_project'),
    path('delete/<int:id>', views.delete_project, name='delete_project'),
]