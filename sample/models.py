from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# CHANGES MADE HERE SHOULD BE REFLECTED IN URLS AND SITEMAPS.PY TOO PLS....
CATEGORY_CHOICES = (
    ("Anime", "Anime"),
    ("Sports", "Sports"),
    ("Hollywood", "Hollywood"),
    ("Bollywood", "Bollywood"),
    ("Netflix", "Netflix")
)

class Article(models.Model):
    title = models.CharField(max_length=3000,null=False,blank=True)
    category = models.CharField(max_length=200, choices= CATEGORY_CHOICES, default= "Unknown")
    slug = models.SlugField(unique=True, max_length=7000)

    relevant_img_url = models.URLField(max_length=1000,null=True,blank=True)
    a_cover = models.ImageField(upload_to='article_covers/',null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.category}-{self.title}'

    def get_absolute_url(self):
        return reverse("view_slides", kwargs={"slug": slugify(self.title)})
    
    
class Slide(models.Model):
    is_p = models.BooleanField(default=False,null=True,blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    s_cover = models.ImageField(upload_to='slides/',null=True,blank=True)

    article = models.ForeignKey(Article ,related_name='sub_slides',on_delete=CASCADE)


    def __str__(self):
        return self.content



