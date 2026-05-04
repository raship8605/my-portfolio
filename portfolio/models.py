from django.db import models

# Create your models here.

class Project(models.model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technology=models.CharField(max_length=200)
    github_link=models.URLField(blank=True)
    live_link=models.URLField(blank=True)
    image=models.ImageField(upload_to='projects/')
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skills(models.model):
    name=models.CharField(max_length=100)
    percentage=models.IntegerField(help_text="Skill proficiency % ")
    category=models.CharField(max_length=50, choice=[
        ('backend', 'Backend'),
        ('frontend','Frontend'),
        ('database','Database'),
        ('ml','Machine Learning'),

    ])
    
    def __str__(self):
        return self.name