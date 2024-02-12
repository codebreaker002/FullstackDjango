from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    stock_status = models.CharField(max_length=50)  # You might want to use choices field here
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name


Category.objects.bulk_create([
    Category(name='Electronics'),
    Category(name='Clothing'),
    Category(name='Books'),
])

# Adding sample tags
Tag.objects.bulk_create([
    Tag(name='Technology'),
    Tag(name='Fashion'),
    Tag(name='Science'),
])