from urllib import request
from apscheduler.schedulers.background import BackgroundScheduler
import tzlocal, math, feedparser, time
from .models import Article,Slide
from bs4 import BeautifulSoup
import requests
from django.utils.text import slugify
from random import randint
from .models import CATEGORY_CHOICES


categories_available = list(dict(CATEGORY_CHOICES).keys())


def start():
    global scheduler
    scheduler =  BackgroundScheduler(timezone=str(tzlocal.get_localzone()))

    for category in categories_available:
        scheduler.add_job(update_db, 'interval',[category],seconds = 3, id=category)

    # scheduler.start()


def update_db(category):
    scheduler.get_job(category).pause()

    if category == 'General':
        return

    FEED_URL = f'https://jiofilocalhtml.work/category/{category.lower()}/feed'

    print(f"{category} Scheduler started and paused.....")
    print(FEED_URL)
    rss = feedparser.parse(FEED_URL)
    already_updated = False
    try:
        first_entry = rss.entries[0]
        for article in Article.objects.all():
            if first_entry.title == article.title:
                already_updated = True
                print(first_entry.title)
                print(f"{category}------------ALREADY UPDATED-----------")
                break
    except IndexError: # EMPTY FEED
        print(f"{category}---------EMPTY FEED")
        pass

    existing_titles = []
    for article in Article.objects.all():
        existing_titles.append(article.title)
    

    if not already_updated:
        for entry in rss.entries:
            if entry.title not in existing_titles:
            # if entry.title in existing_titles:
                print(entry.title)

                rel_url = requests.get(f'https://jiofilocalhtml.work/{slugify(entry.title)}').text
                soup = BeautifulSoup(rel_url, 'lxml')
                try:
                    parent_div = soup.find('div', class_='post-thumb-img-content')
                    img = parent_div.find('img')
                    newArticle = Article(title = entry.title,category = category, relevant_img_url=img['src'], slug = slugify(entry.title))

                except AttributeError:
                    WIDTH = 720
                    HEIGHT  = 1280
                    PICSUM_URL = f"https://picsum.photos/{WIDTH}/{HEIGHT}"
                    newArticle = Article(title = entry.title,category = category, relevant_img_url= PICSUM_URL, slug = slugify(entry.title))

                newArticle.save()

                existing_titles.append(entry.title)
                content = entry.content[0].value
                source = BeautifulSoup(content,'lxml')
                texts = source.get_text()
                all = texts.split('\n')
                all = [i for i in all if not i.isspace()]
                all = [i for i in all if i]
                x = 2
                sublist = [all[n:n+x] for n in range(0, len(all), x)]
                
                while len(sublist) > 12:
                    x += 1
                    sublist = [all[n:n+x] for n in range(0, len(all), x)]

                for b in sublist:
                    slide_text = ' '.join(b)
                    if len(slide_text) <= 200:
                        newSlide = Slide(content = str(slide_text),article = newArticle)
                    else:
                        if len(slide_text) > 500:
                            chopped = slide_text[490:].find(' ')
                            slide_text = slide_text[:490+chopped] + '...'
                        newSlide = Slide(is_p=True,content = str(slide_text),article = newArticle)
                    newSlide.save()


                putSleep(randint(3,10), category)
    
    putSleep(randint(600, 1200), category) # logically setting the timer, the next call will happen (600-1200)s + 5s
    scheduler.resume_job(category)


def putSleep(duration, category):
    print(f"{category} - sleep for {math.floor(duration/60)} mins {duration%60} secs started")
    time.sleep(duration)
    print("sleep ended")
    return


