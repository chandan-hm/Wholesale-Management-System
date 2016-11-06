from django.db import models
from django.db.models import Sum


# Create your models here.
class Producer(models.Model):
    prname = models.CharField(max_length=500)
    praddr = models.CharField(max_length=500)

    def __str__(self):
        return self.prname


class Phoneprod(models.Model):
    pid = models.ForeignKey(Producer, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=15)


class Product(models.Model):
    pname = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()

    def __str__(self):
        return (self.pname + " - Rs." + (str)(self.price))


class Customer(models.Model):
    cname = models.CharField(max_length=200)
    caddr = models.CharField(max_length=200)

    def __str__(self):
        return (self.cname + " - " + self.caddr)


class Phonecus(models.Model):
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=15)

    def __str__(self):
        return self.cid.cname + " - " + self.phoneno


class Receipt(models.Model):
    receiptid = models.IntegerField()


class Cart(models.Model):
    cartno = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    pid = models.ForeignKey(Product)

    def __str__(self):
        return ((str)(self.cartno) + " - " + self.pid.pname)


class Payment(models.Model):
    paymentid = models.CharField(primary_key=True, max_length=100)
    bankname = models.CharField(max_length=200)
    cardno = models.CharField(max_length=100)
    receiptno = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return (self.paymentid + " - " + self.bankname)


class Sells(models.Model):
    receiptno = models.ForeignKey(Receipt)
    prid = models.ForeignKey(Producer)
    pid = models.ForeignKey(Product)


class Pays(models.Model):
    paymentid = models.ForeignKey(Payment)
    cid = models.ForeignKey(Customer)


class Buys(models.Model):
    cid = models.ForeignKey(Customer)
    receiptno = models.ForeignKey(Receipt)
