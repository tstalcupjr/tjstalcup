from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class PortfolioCategory(models.Model):
    #use this model for Design, Development, System Administration
    name=models.CharField(max_length=255)
    description=models.TextField()
    slug=models.SlugField(max_length=100,blank=True)
    
    def __str__(self):
        return "%s" % (self.name)
    
    def save(self, *pargs, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(PortfolioCategory,self).save(*pargs, **kwargs)
    
class PortfolioClassification(models.Model):
    #use this model for PHP, Python, Photoshop, Terminal
    name=models.CharField(max_length=255)
    category=models.ForeignKey(PortfolioCategory)
    description=models.TextField()
    slug=models.SlugField(max_length=100,blank=True)
    
    def __str__(self):
        return "%s" % (self.name)
    
    def save(self, *pargs, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(PortfolioClassification,self).save(*pargs, **kwargs)
    
class PortfolioItem(models.Model):
    #use this model for wswa.org, tom's logo, cron job
    name=models.CharField(max_length=255)
    year=models.CharField(max_length=4)
    classification=models.ForeignKey(PortfolioClassification)
    description=models.TextField()
    slug=models.SlugField(max_length=100,blank=True)
    
    def __str__(self):
        return "%s" % (self.name)
    
    def save(self, *pargs, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(PortfolioItem,self).save(*pargs, **kwargs)
