from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    quantity = models.PositiveIntegerField(default=0)


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)


