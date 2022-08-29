from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
        
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, related_name='products' ,on_delete=models.CASCADE)
    price=models.IntegerField()
    description=models.TextField()
    available=models.IntegerField()
    img_url=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.name