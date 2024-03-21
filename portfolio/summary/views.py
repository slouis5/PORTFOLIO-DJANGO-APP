from django.shortcuts import render, HttpResponse
from .models import Company, SkillCategory, Me, Service, Social

# Views
def index(request):
    companies_logo = Company.objects.all()
    skills_cat = SkillCategory.objects.all()
    gen_desc = Me.objects.all()[:1].get()
    services = Service.objects.all()
    socials = Social.objects.all()
    return render(request, "summary/index.html", { 'companies': companies_logo, 'skills_categories': skills_cat, 'about': gen_desc,
                                                  "services": services, "socials": socials})


