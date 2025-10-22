from rest_framework import serializers
from .models import Skill
from .models import LearningLog

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields= ['id', 'name', 'description', 'created_at']

class LearningLogSerializer(serializers.ModelSerializer):
    skill_name = serializers.ReadOnlyField(source='skill.name')

    class Meta:
        model = LearningLog
        fields = ['id', 'skill', 'skill_name', 'notes', 'hours_spent', 'date']