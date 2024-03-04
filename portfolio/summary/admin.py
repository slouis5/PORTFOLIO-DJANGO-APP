from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'sigle', 'website_url', ]

@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ['about', 'main_title',]

@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', ]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'title', 'period_start', 'period_end', ]

@admin.register(CertificationProvider)
class CertificationProviderAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', ]

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill_group', 'category', ]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', ]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'period_start', ]

