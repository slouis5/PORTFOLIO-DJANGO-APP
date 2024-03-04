from django.shortcuts import render, HttpResponse
from .models import Company

# Views
def index(request):
    companies_logo = Company.objects.all()
    return render(request, "summary/index.html", { 'companies': companies_logo, })
