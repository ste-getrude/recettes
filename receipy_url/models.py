from django.db import models

# Create your models here.
class ReceipyUrl(models.Model):
    scheme = models.CharField(max_length=10)
    netloc = models.CharField(max_length=200)
    path = models.CharField(max_length=400)
    params = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    fragment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.netloc
    
class Receipy(models.Model):
    receipy_url = models.URLField(max_length=400, blank=True)
    receipy_title = models.CharField(max_length=100) 
    receipy_yield = models.SmallIntegerField() # pas claire, peut etre string
    
    
class RawIngredientLine(models.Model):
    receipy = models.ForeignKey(Receipy, on_delete=models.CASCADE)
    qty = models.CharField(max_length=100, blank=True) 
    ingredient = models.CharField(max_length=100) 
    detail = models.CharField(max_length=100, blank=True) 
    
    

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    
class SiVolume(models.Model):
    pass

class ImperialVolume(models.Model):
    pass
    
class ReceipyIngredient(models.Model):
    receipy = models.ForeignKey(Receipy, on_delete=models.CASCADE)
    qty = models.FloatField()
    unit = models.CharField(max_length=100, blank=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    
class ReceipySteps(models.Model):
    receipy = models.ForeignKey(Receipy, on_delete=models.CASCADE)
    steps = models.TextField()
    
    
    
    
    