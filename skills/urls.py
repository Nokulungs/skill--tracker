from django.urls import path
from .views import SkillListCreateView, LearningLogListCreateView
from .views import SkillListCreateView, SkillDetailView

urlpatterns = [
    path('skills/', SkillListCreateView.as_view(), name='skill-list'),
    path('logs/', LearningLogListCreateView.as_view(), name='log-list'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
]
