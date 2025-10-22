from django.shortcuts import render
from .models import Skill, LearningLog
from rest_framework import generics

from .serializer import SkillSerializer, LearningLogSerializer
# Create your views here.

class SkillListCreateView(generics.ListCreateAPIView):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

class LearningLogListCreateView(generics.ListCreateAPIView):
    queryset = LearningLog.objects.all()
    serializer_class = LearningLogSerializer
    
class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer