from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sample import views as sample_views
from sample.sitemaps import CategorySitemap, AnimeSiteMap, SportsSiteMap, HollywoodSiteMap, BollywoodSiteMap, NetflixSiteMap
from django.contrib.sitemaps.views import sitemap, index

sitemaps = {
    'categories': CategorySitemap,

    'Anime' : AnimeSiteMap,
    'Sports' : SportsSiteMap,
    'Hollywood' : HollywoodSiteMap,
    'Bollywood' : BollywoodSiteMap,
    'Netflix' : NetflixSiteMap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sample_views.home , name="home"),
    path('privacy-policy/', sample_views.privacy, name="privacy_policy"),
    path('about-us/', sample_views.about, name="about_us"),
    path('contact-us/', sample_views.contact, name="contact_us"),
    path('cookies-policy/', sample_views.cookies, name="cookies_policy"),

    path('story/<str:slug>/', sample_views.slides , name="view_slides"),


    path('sitemap.xml/', index , {'sitemaps': sitemaps,'template_name':'sitemapindex.xml','content_type':'application/xml','sitemap_url_name': 'another'}, name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml/', sitemap , {'sitemaps': sitemaps, 'template_name':'sitemap1.xml','content_type':'application/xml'}, name='another'),


    path('category/<str:category>/', sample_views.category , name="view_category"),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)