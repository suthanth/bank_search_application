from django.db import models


class banks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=49)

    class Meta:
        ordering = ['id']


class branches(models.Model):
    ifsc = models.CharField(max_length=19, primary_key=True)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank = models.ForeignKey(banks, on_delete=models.CASCADE, related_name='banks', null=True)

    class Meta:
        ordering = ['ifsc']

    @property
    def bank_details(self):
        return self.bank_id
