from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Warehouse(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="products")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="product")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="product")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

