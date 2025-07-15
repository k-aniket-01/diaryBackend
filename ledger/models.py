# ledger/models.py

from django.db import models

class LedgerHead(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

class Party(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)
    opening_balance = models.FloatField(default=0)
    ledger = models.ForeignKey(LedgerHead, on_delete=models.SET_NULL, null=True, blank=True)

class Payment(models.Model):
    date = models.DateField()
    ledger = models.ForeignKey(LedgerHead, on_delete=models.SET_NULL, null=True, blank=True)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField()
    status = models.CharField(max_length=20, default="Paid")
    remark = models.TextField(blank=True, null=True)
    remaining_amount = models.FloatField(default=0)

class Receipt(models.Model):
    date = models.DateField()
    ledger = models.ForeignKey(LedgerHead, on_delete=models.SET_NULL, null=True, blank=True)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField()
    status = models.CharField(max_length=20, default="Paid")
    remark = models.TextField(blank=True, null=True)
    remaining_amount = models.FloatField(default=0)

class PartialPayment(models.Model):
    parent_id = models.IntegerField()  # You'll adjust this based on design
    type = models.CharField(max_length=20)  # 'payment' or 'receipt'
    date = models.DateField()
    amount_paid = models.FloatField()
    remark = models.TextField(blank=True, null=True)
