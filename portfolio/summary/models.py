from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Company(models.Model):
    sigle = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    website_url = models.URLField()
    logo_local = models.ImageField(upload_to='company_logo_og/')
    logo_ext_url = models.URLField(blank=True, null=True)

    def __str__(self,):
        return self.name
    
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Me(models.Model):
    about = models.CharField(max_length = 700)
    #adress = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 18)
    mail = models.EmailField()
    trainnings = models.CharField(max_length = 50)
    main_title = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Me"
        verbose_name_plural = "Me"

class Strength(models.Model):
    name = models.CharField(max_length = 40)
    desc = models.CharField(max_length=350)
    icon = models.FileField(upload_to='strengths_logo/', validators=[FileExtensionValidator(['png', 'svg'])])

    def __str__(self,):
        return self.name

    class Meta:
        verbose_name = 'Strength'
        verbose_name_plural = 'Strengths'

class Education(models.Model):
    school_name = models.CharField(max_length = 120)
    sigle = models.CharField(max_length=20, null=True, blank=True)
    period_start = models.DateField()
    period_end = models.DateField(blank=True, null=True)
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)

    class Meta:
        ordering = ('period_start',)
        verbose_name = 'Study'
        verbose_name_plural = 'Studies'
    
    def __str__(self,):
        return self.school_name

class CertificationProvider(models.Model):
    name = models.CharField(max_length = 120)
    website_url = models.URLField()
    logo = models.ImageField(upload_to='certif_provider_logo_og/')

    class Meta:
        verbose_name = 'Certification Provider'
        verbose_name_plural = 'Certification Providers'

    def __str__(self,):
        return self.name
class Certification(models.Model):
    provider = models.ForeignKey("CertificationProvider", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length = 100)
    url = models.URLField(null=True, blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    get_date = models.DateField(blank=True, null=True)
    certification_file = models.FileField(upload_to='certifications/')

    class Meta:
        ordering = ('get_date', )

    def __str__(self,):
        return self.title
class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='skill_categories/', validators=[FileExtensionValidator(['png', 'svg'])])

    def __str__(self,):
        return self.name

class Skill(models.Model):
    PLATFORM_TOOL_SOFTWARE = "platform_tool_software"
    LANGUAGES = "language"
    SKILL_GROUP_CHOICES = {
        PLATFORM_TOOL_SOFTWARE: "Platforms, Tools and Software",
        LANGUAGES: "Programming Languages",
    }

    
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    LEVEL_CHOICES = {
        BEGINNER : "BEGINNER",
        INTERMEDIATE : "INTERMEDIATE",
        ADVANCED : "ADVANCED"
    }
    name = models.CharField(max_length = 50)
    skill_group = models.CharField(choices = SKILL_GROUP_CHOICES, default=PLATFORM_TOOL_SOFTWARE)
    level = models.CharField(choices = LEVEL_CHOICES, default=INTERMEDIATE)
    category = models.ForeignKey("SkillCategory", on_delete=models.SET_NULL, null=True)

    def __str__(self,):
        return self.name

class Language(models.Model):

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"
    LANG_LEVEL_CHOICES = {
        A1 : "A1",
        A2 : "A2",
        B1 : "B1",
        B2 : "B2",
        C1 : "C1",
        C2 : "C2",
    }
    BEGINNER = "Beginner"
    LOWER_ELEMENTARY = "lower_elementary"
    UPPER_ELEMENTARY = "upper_elementary"
    LOWER_INTERMEDIATE = "lower_intermediate"
    UPPER_INTERMEDIATE = "upper_intermediate"
    LOWER_ADVANCED = "lower_advanced"
    UPPER_ADVANCED = "upper_advanced"
    FLUENT = "fluent"
    PROFICIENT = "proficient"
    EXPERT = "expert"

    LANG_CAT_CHOICES = {
        BEGINNER : "Beginner",
        LOWER_ELEMENTARY : "Lower Elementary",
        UPPER_ELEMENTARY : "Upper Elementary",
        LOWER_INTERMEDIATE : "Lower Intermediate",
        UPPER_INTERMEDIATE : "Upper Intermediate",
        LOWER_ADVANCED : "Lower Advanced",
        UPPER_ADVANCED : "Upper Advanced",
        FLUENT : "Fluent",
        PROFICIENT : "Proficient",
        EXPERT : "Expert / Native",
            }

    name = models.CharField(max_length = 30)
    level = models.CharField(max_length = 2, choices= LANG_LEVEL_CHOICES)
    speaking = models.CharField(max_length = 30, choices= LANG_CAT_CHOICES)
    reading = models.CharField(max_length = 30, choices= LANG_CAT_CHOICES)
    writing = models.CharField(max_length = 30, choices= LANG_CAT_CHOICES)

    def __str__(self,):
        return self.name
class Experience(models.Model):
    is_last = models.BooleanField()
    title = models.CharField(max_length = 30)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=300)
    period_start = models.DateField()
    period_end = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('period_start',)

    def __str__(self,):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=700)
    period_start = models.DateField()
    period_end = models.DateField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    online_url = models.URLField(blank=True, null=True)
    tech_used = models.CharField(max_length=200, null=True, blank=True)
    is_programming_proj = models.BooleanField(default = False)
    image = models.ImageField(upload_to='projects', blank=True)

    def __str__(self,):
        return self.title