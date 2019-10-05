from django.db import models

class Profile(models.Model):
    customer = 'customer'
    trainer = 'trainer'
    POSITION_CHOICES = (
        (customer, 'customer'),
        (trainer, 'trainer'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    position = models.CharField(
    max_length=20,
    choices=POSITION_CHOICES, default = customer
    )

class Customer(models.Model):
    name = models.CharField(max_length=70)
    basic='basic'
    pro='pro'
    premium='premium'
    PRICING = (
        (basic,'basic'),
        (pro,'pro'),
        (premium,'premium'), 
    )
    pricing = models.CharField(
    max_length=20,
    choices=PRICING, default = basic
    )
    trainerId = models.ForeignKey(Trainer, on_delete = models.PROTECT)
    mealId = models.ForeignKey(Meals, on_delete = models.PROTECT)

class Trainer(models.Model):
    name = models.CharField(max_length=70)
    type = models.ForeignKey(Meals, on_delete = models.PROTECT)
    salary = models.IntegerField()
    rating = models.IntegerField()

class Meals(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField(max_length = 500)