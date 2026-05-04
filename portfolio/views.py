from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all().order_by('-created_date')
    skills = Skill.objects.all()
    
    # Your personal data 
    context = {
        'name': 'Pardeshi Rashi Ramnarayan',  
        'title': 'Python Full Stack Developer',
        'bio': 'BCS Graduate 2026 | Python | Django | SQL Enthusiast',
        'email': 'rashipardeshi870@gmail.com',
        'phone': '+91 8767699147',
        'location': 'Pune, India',
        'github': 'https://github.com/raship8605',
        'linkedin': 'https://www.linkedin.com/in/pardeshi-rashi8605/',
        'projects': projects,
        'skills': skills,
        'education': [
            {'degree': 'BCS (Computer Science)', 
             'college': 'MGMs college of CS and IT, Nanded', 
             'year': '2023-2026',
             'percentage': '85%'},
            {'degree': 'HSC', 
             'college': 'Shree shivaji junoir college', 
             'year': '2021-2023',
             'percentage': '69%'},
        ],
        'certifications': [
            'Python Full Stack - Kiran Academy, Pune',
            
        ]
    }
    return render(request, 'portfolio/home.html', context)