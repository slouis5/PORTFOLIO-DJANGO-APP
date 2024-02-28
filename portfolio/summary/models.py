from django.db import models

# Create your models here.
class Company(models.Model):
    sigle = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    website_url = models.URLField()
    logo_local = models.ImageField(upload_to='media/company_logo_og/')
    logo_ext_url = models.URLField()

    def __str__(self,):
        return self.name
