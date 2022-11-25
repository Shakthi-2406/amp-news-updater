from django.shortcuts import render, HttpResponseRedirect
from .models import Article,Slide
import random
from django.core.paginator import Paginator
import re
from .models import CATEGORY_CHOICES

categories_available = list(dict(CATEGORY_CHOICES).keys())

font_list = ['Aclonica', 'Amaranth', 'Architects Daughter', 'El Messiri', 'Handlee', 'IBM Plex Sans Thai Looped', 'IM Fell English SC', 'Itim', 'Kalam', 'Kaushan Script','Quintessential', 'Roboto', 'Roboto Condensed', 'Ruda', 'Source Serif 4', 'Special Elite', 'Supermercado One','Work Sans' ]


def home(request):
    if is_mobile(request):
        pages = Paginator(Article.objects.all().order_by("-date"), 8)
    else:
        pages = Paginator(Article.objects.all().order_by("-date"), 12)
    current_page = request.GET.get('page')
    articles = pages.get_page(current_page)
    hue = random.randint(0,359)
    context = {
        'articles': articles,
        'hue': hue,
        'categories': categories_available,
        'current_category': 'Mixed'.capitalize()
    }
    return render(request, 'sample/merged.html', context)



def privacy(request):
    return render(request, 'sample/privacy-policy.html')

def about(request):
    return render(request, 'sample/about-us.html')

def contact(request):
    return render(request, 'sample/contact-us.html')

def cookies(request):
    return render(request, 'sample/cookies-policy.html')


def category(request, category):

    if is_mobile(request):
        pages = Paginator(Article.objects.all().filter(category = category.capitalize()).order_by("-date"), 8)
    else:
        pages = Paginator(Article.objects.all().filter(category = category.capitalize()).order_by("-date"), 12)
    current_page = request.GET.get('page')
    articles = pages.get_page(current_page)
    hue = random.randint(0,359)


    context = {
        'articles': articles,
        'hue': hue,
        'categories': categories_available,
        'current_category': category.capitalize()
    }
    return render(request, 'sample/merged.html', context)



def slides(request,slug):

    article = Article.objects.all().get(slug = slug)
    pk = article.id
    slides = article.sub_slides.all()
    available_data = Article.objects.all().order_by("-date")
    array = []
    for data in available_data:
        array.append(data.id)
    upper = len(array)
    current_index = array.index(pk)
    if current_index == upper-1:
        next = array[0]
    else:
        next = array[current_index+1]
    nextArticle = Article.objects.get(pk = next)
    
    context = {
        'fonts': font_list,
        'article':article,
        'nextArticle':nextArticle ,
        'slides':slides}
    return render(request, 'sample/slides_amp.html', context)

def is_mobile(request):

    MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False




   
    