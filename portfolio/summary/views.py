from django.shortcuts import render, HttpResponse
from .models import Company, SkillCategory

# Views
def index(request):
    companies_logo = Company.objects.all()
    skills_cat = SkillCategory.objects.all()
    return render(request, "summary/index.html", { 'companies': companies_logo, 'skills_categories': skills_cat})


