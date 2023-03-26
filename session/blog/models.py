from django.db import models



# Create your models here.
class Blog(models.Model):
    LANGUAGE_ENGLISH='en'
    LANGUAGE_KOREAN='kr'
    title =models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='')
    LANGUAGE_CHOICE=((LANGUAGE_ENGLISH,'English'),(LANGUAGE_KOREAN,'Korean'))
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, blank=True, default=LANGUAGE_ENGLISH)
    introduce = models.TextField()
    birthday= models.DateField(default='2000-01-01')
    email= models.EmailField(max_length=100, blank=True, default='')
    picture= models.ImageField(upload_to='blog_pics', blank=True) 



    def __str__(self) :
        return self.title
    
