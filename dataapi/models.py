from MySQLdb import TIMESTAMP
from django.db import models

class Securities(models.Model):
    SYMBOL = models.CharField(max_length=15)
    NAME_OF_COMPANY = models.CharField(max_length=100)
    SERIES = models.CharField(max_length=2)
    DATE_OF_LISTING = models.TextField(max_length=20)
    PAID_UP_VALUE = models.IntegerField()
    MARKET_LOT = models.IntegerField()
    ISIN_NUMBER = models.CharField(max_length=15)
    FACE_VALUE = models.IntegerField()

    def __str__(self):
        return self.SYMBOL

class DateBhav(models.Model):
    Date = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.Date

class Bhav(models.Model):
    SYMBOL = models.CharField(max_length=15)
    SERIES = models.CharField(max_length=2)
    OPEN = models.FloatField()
    HIGH = models.FloatField()
    LOW = models.FloatField()
    CLOSE = models.FloatField()
    LAST = models.FloatField()
    PREVCLOSE = models.FloatField()
    TOTTRDQTY = models.IntegerField()
    TOTTRDVAL = models.FloatField()
    TIMESTAMP = models.ForeignKey(DateBhav,related_name='SYMBOL', on_delete=models.CASCADE)
    TOTALTRADES = models.IntegerField()
    ISIN = models.CharField(max_length=25)

    def __str__(self):
        return self.SYMBOL    


