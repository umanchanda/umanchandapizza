from django.db import models

# Create your models here.
class Pizza(models.Model):
    choice = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"You ordered a {self.size} {self.choice} pizza for ${self.price}"

class Sub(models.Model):
    size = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"You ordered a {self.size} sub for ${self.price}"

class Pasta(models.Model):
    form = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"You ordered a Baked Ziti with {self.form} for ${self.price}"

class Topping(models.Model):
    topping = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"You ordered a {self.topping} topping for ${self.price}"

class Salad(models.Model):
    salad = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"You ordered a {self.salad} salad for ${self.price}"

class DinnerPlatter(models.Model):
    dinnerplatter = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"You ordered a {self.size} {self.dinnerplatter} dinner platter for ${self.price}"