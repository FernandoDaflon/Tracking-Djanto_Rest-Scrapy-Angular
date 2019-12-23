from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class U_tracking_return(models.Model):
    ori = models.CharField(max_length=3)
    des = models.CharField(max_length=3)
    eta = models.CharField(max_length=100, null=True)
    etd = models.CharField(max_length=100, null=True)
    flight_no = models.CharField(max_length=10)
    status = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.ori, self.des, self.eta, self.etd, self.flight_no, self.status)


class Awb(models.Model):
    awb_no = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    awbs_list = models.ManyToManyField(U_tracking_return)

    def __str__(self):
        return self.awb_no, self.user, self.awbs_list
