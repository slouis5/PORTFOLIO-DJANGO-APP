from django.shortcuts import render, HttpResponse
from .models import Company, SkillCategory, Me, Service, Social, Experience



def footer():
    companies_logo = Company.objects.all()
    services = Service.objects.all()
    socials = Social.objects.all()
    return dict({'companies': companies_logo, "services": services, "socials": socials})

# Views
def index(request):
    skills_cat = SkillCategory.objects.all()
    gen_desc = Me.objects.all()[:1].get()
    actual_title = Experience.objects.filter(is_last=True)
    return render(request, "summary/index.html", {'skills_categories': skills_cat, 'about': gen_desc,
                                                  'current_title':actual_title} | footer())


def experience(request):
    experiences = Experience.objects.all().order_by('-period_start',)

    return render(request, 'summary/experiences.html', {'experiences': experiences} | footer())

