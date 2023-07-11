# THIRD PARTY IMPORTS
from django.urls import path

# PROJECT IMPORTS
from . import views


urlpatterns = [
    # EXERCISE PATHS
    path('exercise', views.ExercisesViews.as_view(), name='get all and post'),
    path('exercise/<int:pk>', views.ExerciseDetail.as_view(), name='read, update and delete by id'),

    # ANSWER PATHS
    path('answer', views.AnswerViews.as_view(), name='get all and post'),
    path('answer/<int:pk>', views.ExerciseDetail.as_view(), name='read, update and delete by id'),
]
