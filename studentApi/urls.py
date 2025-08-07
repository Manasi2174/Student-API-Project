from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    path('student/create/',CreateStudent.as_view()),
    path('student/list/',ListStudents.as_view()),
    path('student/<int:pk>/',GetStudentById.as_view()),
    path('student/update/<int:pk>/',UpdateStudent.as_view()),
    path('student/delete/<int:pk>/',DeleteStudent.as_view()),
    path('student/by-name/<str:name>/',GetStudentByName.as_view()),
    path('student/by-roll-range/<int:min_roll>/<int:max_roll>/',GetByRollRange.as_view()),
    path('student/get-count/',GetTotalCount.as_view()),
    path('student/get-by-partial/<str:query>/',GetByPartial.as_view()),
    path('student/topper/',GetToppers.as_view()),
]