from .models import Article,Slide
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import urllib.request
from souq.settings import BASE_DIR
import shutil


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()


# width=450, height=300
WIDTH = 720
HEIGHT  = 1280
PICSUM_URL = f"https://picsum.photos/{WIDTH}/{HEIGHT}"

def relevant_jpg(i, REL_URL):
    try:
        filename = f'image-{i}.jpg'
        full_path = f'{BASE_DIR}/media/{filename}'

        with opener.open(REL_URL) as response, open(full_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            out_file.close()

        return filename
    except:
        return url_to_jpg(i)

def url_to_jpg(i):
    filename = f'image-{i}.jpg'
    full_path = f'{BASE_DIR}/media/{filename}'
    urllib.request.urlretrieve(PICSUM_URL,full_path)
    return filename

@receiver(post_save, sender=Article)
def article_save_create_cover(sender, instance, *args, **kwargs):
    if not instance.a_cover:
        try:
            instance.a_cover = relevant_jpg(f'A{instance.id}', instance.relevant_img_url)

        except:
            instance.a_cover = url_to_jpg(f'A{instance.id}')
        instance.save()

@receiver(post_save, sender=Slide)
def slide_save_create_cover(sender, created, instance, *args, **kwargs):
    if not instance.s_cover:
        instance.s_cover = url_to_jpg(f'S{instance.id}')
        instance.save()

@receiver(post_delete, sender=Article)
def art_del_img_del(sender, instance, **kwargs):
    if instance.a_cover:
        instance.a_cover.delete(False)

@receiver(post_delete, sender=Slide)
def art_del_img_del(sender, instance, **kwargs):
    if instance.s_cover:
        instance.s_cover.delete(False)