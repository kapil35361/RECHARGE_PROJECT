from django.db import models

class Airtelplans(models.Model):
    price=models.FloatField()
    validity=models.CharField(max_length=10)
    sms=models.IntegerField()
    data=models.CharField(max_length=20)
    postpaid=models.BooleanField()

    def __str__(self) :
        return f'{self.price}'


class VIplans(models.Model):
    price=models.FloatField()
    validity=models.CharField(max_length=10)
    sms=models.IntegerField()
    data=models.CharField(max_length=20)
    postpaid=models.BooleanField()

    def __str__(self) :
        return f'{self.price}'



class Jioplans(models.Model):
    price=models.FloatField()
    validity=models.CharField(max_length=10)
    sms=models.IntegerField()
    data=models.CharField(max_length=20)
    postpaid=models.BooleanField()

    def __str__(self) :
        return f'{self.price}'



class recharge(models.Model):
    
    Airtelplans=models.ForeignKey(Airtelplans,on_delete=models.CASCADE)
    VIplans=models.ForeignKey(VIplans,on_delete=models.CASCADE)
    Jioplans=models.ForeignKey(Jioplans,on_delete=models.CASCADE)


