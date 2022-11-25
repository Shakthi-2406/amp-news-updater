from django.contrib.sitemaps import Sitemap

from sample.views import category
from .models import Article, CATEGORY_CHOICES
from django.urls import reverse

categories_available = list(dict(CATEGORY_CHOICES).keys())


class CategorySitemap(Sitemap):
    def items(self):
        return categories_available
    
    def location(self, item):
        return reverse('view_category', kwargs={'category': item})

class GeneralSiteMap(Sitemap):
    def items(self):
        return Article.objects.all().filter(category = 'General')

class AnimeSiteMap(Sitemap):
    def items(self):
        return Article.objects.all().filter(category = 'Anime')

class SportsSiteMap(Sitemap):
    def items(self):
        return Article.objects.all().filter(category = 'Sports')

class HollywoodSiteMap(Sitemap):
    def items(self):
        return Article.objects.all().filter(category = 'Hollywood')

class BollywoodSiteMap(Sitemap):
    def items(self):
        return Article.objects.all().filter(category = 'Bollywood')

class NetflixSiteMap(Sitemap):
    def items(self):
        return Article.objects.all().filter(category = 'Netflix')