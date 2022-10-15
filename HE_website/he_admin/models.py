from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alpha characters are allowed.')
#Product Category table


class ProductCategory(models.Model):
    category       = models.CharField(max_length=50,unique=True,null=False,blank=False)
    description    = models.TextField(max_length=2000,null=False,blank=False)
    category_image = models.ImageField(upload_to = 'category_pictures',height_field=None,width_field=None,null=False,blank=False)
    status         = models.BooleanField(default=1,blank=False,null=False)
    created_date   = models.DateTimeField(auto_now_add=True)
    updated_date   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class Products(models.Model):
    alphaspaces = RegexValidator(r'^[a-zA-z ]+$',"Only letters are allowed in Product Name") #letters and spaces regular expression
    category     = models.ForeignKey("he_admin.ProductCategory",on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50,blank=False,null=False,validators=[alphaspaces])
    Image_alt    = models.CharField(max_length=50,blank=True) 
    image        = models.ImageField(upload_to="product_pictures", height_field=None, width_field=None, max_length=None)
    status= models.BooleanField(default=1,blank=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

