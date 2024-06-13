from django.contrib import admin
from django.urls import path, include
from task.views import home

urlpatterns = [
    path('', home, name='home'),  # Redirect root URL to show_tasks
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('categories/', include('category.urls')),
]
