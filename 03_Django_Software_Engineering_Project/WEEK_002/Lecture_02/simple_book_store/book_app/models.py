from django.db import models
import random
def create_new_ref_number():
        return random.randint(0, 9999)



# Create your models here.

class BookStoreModel(models.Model):

    CATEGORY_CHOICES = [
        ('western', 'Western'),
        ('revenge', 'Revenge'),
        ('spaghetti_western', 'Spaghetti Western'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('historical', 'Historical'),
        ('adventure', 'Adventure'),
        ('crime', 'Crime'),
        ('thriller', 'Thriller'),
        ('noir', 'Noir'),
        ('romance', 'Romance'),
        ('neo_western', 'Neo-Western'),
        ('martial_arts', 'Martial Arts'),
        ('ensemble_cast', 'Ensemble Cast'),
        ('fantasy', 'Fantasy'),
        ('comedy', 'Comedy'),
        ('redemption', 'Redemption'),
        ('classic', 'Classic'),
        ('biographical', 'Biographical'),
        ('tragedy', 'Tragedy'),
    ]
    id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=40)
    catagory=models.CharField(max_length=75,choices=CATEGORY_CHOICES)
    first_published=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True,)
    isbn = models.CharField(
           max_length = 75,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number
      )