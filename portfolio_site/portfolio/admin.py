from django.contrib import admin
from portfolio_site.portfolio import models

class PortfolioItemAdmin(admin.ModelAdmin):
    pass

class PortfolioClassificationAdmin(admin.ModelAdmin):
    pass

class PortfolioCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=["name","description","slug"]

admin.site.register(models.PortfolioItem, PortfolioItemAdmin)
admin.site.register(models.PortfolioClassification, PortfolioClassificationAdmin)
admin.site.register(models.PortfolioCategory, PortfolioCategoryAdmin)