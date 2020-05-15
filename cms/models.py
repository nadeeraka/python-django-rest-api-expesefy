from datetime import datetime
from typing import List, Tuple
from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    name = models.ForeignKey("IncomeType", default='', on_delete=models.CASCADE, related_name="incomes")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    name = models.ForeignKey("ExpenseType", on_delete=models.CASCADE, related_name="expenses")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Saving(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    name = models.ForeignKey('SavingType', on_delete=models.CASCADE, related_name="savings")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    rate = models.DecimalField(max_digits=100, decimal_places=4, default=0)

    class Meta:
        ordering = ['id']


class ExpenseType(models.Model):
    EXPENSE_CHOICES = [
        ('L', 'Lifestyle'),
        ('E', 'Entertainment'),
        ('D', 'Donation'),
        ('ED', 'Eduction'),
        ('O', 'Other'),
        ('F', 'Fixed'),
        ('EQ', 'Equipment'),

    ]
    name = models.CharField(max_length=2, default='Salary', choices=EXPENSE_CHOICES)

    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['id']


class SavingType(models.Model):
    SAVING_CHOICES = [
        ('B', 'Bank'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=2, default='Bank', choices=SAVING_CHOICES)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['id']


class IncomeType(models.Model):
    INCOME_CHOICES = {
        ('S', 'Salary'),
        ('P', 'Property'),
        ('B', 'Business'),
        ('O', 'Other')
    }

    name = models.CharField(max_length=2, default='Salary', choices=INCOME_CHOICES)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['id']


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)

    class Meta:
        ordering = ['id']