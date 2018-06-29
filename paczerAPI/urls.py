from django.urls import path
from . import views

urlpatterns = [
    path('<owner>/<repositoryName>', views.gitRead),
]

