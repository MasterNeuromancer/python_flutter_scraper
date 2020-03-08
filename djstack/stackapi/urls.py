from django.urls import path, include
from .views import index, QuestionApi, latest
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionApi)

urlpatterns = [
    path('', index,name='index'),
    path('', include(router.urls)),
    path('latest', latest, name='latest'),
]
