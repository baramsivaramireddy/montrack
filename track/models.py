from django.db import models

# Create your models here.


class took(models.Model):
    amount     =     models.DecimalField(max_digits=20,decimal_places=5)
    purpose    =     models.TextField()
    dataTime   =     models.DateTimeField(auto_now_add=True, blank=True)

    
    class Meta:
     
        verbose_name = 'take'



class gave(models.Model):
    amount     =     models.DecimalField(max_digits=20,decimal_places=5)
    purpose    =     models.TextField()
    dataTime   =     models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
     
        verbose_name = 'give'

    
    

class stats(models.Model):
    took        =       models.DecimalField(max_digits=20,decimal_places=5 ,default=0)
    gave        =       models.DecimalField(max_digits=20,decimal_places=5,default=0)
    class Meta:
     
        verbose_name = 'statistic'
