from django.urls import path
from . import views
urlpatterns = [
    path('stuinfo/<int:pk>', views.student_detail),
    path('stuinfo/', views.student_list),
    path('stucreate/', views.student_create),
]