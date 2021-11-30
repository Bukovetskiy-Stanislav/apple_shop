from django.db import models
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import os

# Create your models here.



class Category(models.Model):
    name= models.CharField(max_length=250, unique=True)
    slug= models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image= models.ImageField(upload_to='category', blank=True) 

    class Meta:
        ordering= ('name', )
        verbose_name= 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


def img_directory_path(self, filename):
      return os.path.join(
      "%s" % self.category.slug, "%s" % self.slug, filename) 


class Product(models.Model):
    name= models.CharField(max_length=250, unique=True)
    slug= models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to= img_directory_path , blank=True) 
    stock= models.IntegerField()
    available= models.BooleanField(default=True)
    created= models.DateField(auto_now_add=True)
    updated= models.DateField(auto_now=True)

    class Meta:
        ordering= ('name', )
        verbose_name= 'product'
        verbose_name_plural = 'products'


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

class MacBook(Product):
    color = models.TextField(max_length=200,blank=True, verbose_name='Color')
    display = models.TextField(max_length=1000,blank=True, verbose_name='Display')
    chip = models.TextField(max_length=255,blank=True, verbose_name='Chip')
    battery_and_power = models.TextField(max_length=255,blank=True, verbose_name='Battery and Power')
    charging = models.TextField(max_length=255,blank=True, verbose_name='Charg­ing and Expan­sion')
    memory = models.TextField(max_length=255,blank=True, verbose_name='Memory')
    storage = models.TextField(max_length=255,blank=True, verbose_name='Storage')
    keyboard_and_trackpad = models.TextField(max_length=1000,blank=True, verbose_name='Key­board and Track­pad')
    toch_id = models.TextField(max_length=1000,blank=True, verbose_name='Touch ID')
    wireless = models.TextField(max_length=1000,blank=True, verbose_name='Wireless')
    camera = models.TextField(max_length=1000,blank=True, verbose_name='Camera')
    video_support = models.TextField(max_length=1000,blank=True, verbose_name='Video Support')
    audio = models.TextField(max_length=1000,blank=True, verbose_name='Audio')
    size_and_weight = models.TextField(max_length=1000,blank=True, verbose_name='Size and Weight')



class Iphone(Product):
    color = models.TextField(max_length=2000,blank=True, verbose_name='Color')
    display = models.TextField(max_length=1000,blank=True, verbose_name='Display')
    chip = models.TextField(max_length=2555,blank=True, verbose_name='Chip')
    main_cam_mp = models.TextField(max_length=1000, verbose_name='Главная камера')
    frontal_cam_mp = models.TextField(max_length=1000,blank=True, verbose_name='Фронтальная камера')
    wireless = models.TextField(max_length=1000,blank=True, verbose_name='Cellular and Wireless')
    battery = models.TextField(max_length=255,blank=True, verbose_name='Power and Battery')
    memory = models.CharField(max_length=255,blank=True, verbose_name='Оперативная память')
    storage = models.CharField(max_length=255, null=True, blank=True, verbose_name=' встраивамой памяти')
    sensors = models.TextField(max_length=1000,blank=True, verbose_name='Sensors')
    sim_card = models.TextField(max_length=255,blank=True, verbose_name='SIM Card')
    interfaces = models.CharField(max_length=1000,blank=True, verbose_name='Interfaces')
    weight = models.TextField(max_length=255,blank=True, verbose_name='Size and Weight')



  

    

class Ipad(Product):
    color = models.TextField(max_length=2000,blank=True, verbose_name='Color')
    display = models.TextField(max_length=1000,blank=True, verbose_name='Display')
    chip = models.TextField(max_length=2555,blank=True, verbose_name='Chip')
    camera = models.TextField(max_length=1000,blank=True, verbose_name='Camera')
    wireless = models.TextField(max_length=1000,blank=True, verbose_name='Cellular and Wireless')
    sim_card = models.TextField(max_length=2555,blank=True, verbose_name='SIM Card')
    sensors = models.TextField(max_length=1000,blank=True, verbose_name='Sensors')
    toch_id = models.TextField(max_length=1000,blank=True, verbose_name='Touch ID')
    penc = models.BooleanField(default=True, verbose_name='support apple Pencil')
    battery_and_power = models.TextField(max_length=2555,blank=True, verbose_name='Battery and Power')
    weight = models.TextField(max_length=2555,blank=True, verbose_name='Size and Weight')
    