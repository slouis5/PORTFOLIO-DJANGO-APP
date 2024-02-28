from django.shortcuts import render, HttpResponse

# Views
def index(request):
    return HttpResponse("Hello, world. You're in the home page of summary, the single app of the portfolio project.")
