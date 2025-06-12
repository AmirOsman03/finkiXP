from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from finkiXP_app.views import index, subjects, add_task, subject_tasks, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('subjects/', subjects, name='subjects'),
    path('add-task/', add_task, name='add-task'),
    path('subjects/<int:subject_id>/tasks/', subject_tasks, name='subject-tasks'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
