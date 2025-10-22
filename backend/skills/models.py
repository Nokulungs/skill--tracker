from django.db import models

class Skill(models.Model):
    name= models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name

class LearningLog(models.Model):
    skill= models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='logs')
    notes = models.TextField(blank=True)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.skill.name} -{self.date}"