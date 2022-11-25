from django.contrib import admin
from .models import Article,Slide

class SlideAdmin(admin.TabularInline):
    model = Slide

class ArticleAdmin(admin.ModelAdmin):
    inlines = [SlideAdmin]

admin.site.register(Article,ArticleAdmin)