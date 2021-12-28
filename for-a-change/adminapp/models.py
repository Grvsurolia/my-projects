# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from fundraiser.models import Fundraiser


# Create your models here.

class RequestedUpdateFundraiser(models.Model):
    frid = models.ForeignKey(Fundraiser, on_delete=models.CASCADE)
    frTitle = models.CharField(max_length=200, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)
    # title = models.CharField(max_length=200, blank=False)
    # slug = models.CharField(max_length=50, blank=False)
    # CAMPGAIN_CAUSE = (
    #     ('medical', 'MEDICAL'),
    # )
    # cause = models.CharField(max_length=20, choices=CAMPGAIN_CAUSE)
    # beneficiaryFullName = models.CharField(max_length=50, unique=False)
    # beneficiaryAge = models.PositiveIntegerField(null=False, blank=False)
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Other'),
    # )
    # beneficiaryGender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # cityOfResidence = models.CharField(max_length=100)
    # goalAmount = models.FloatField(null=False,validators=[MinValueValidator(200)])
    # is_active = models.BooleanField(default=False)
    # story = models.TextField(max_length=1000)
    # isPrivate = models.BooleanField(default=False)
    # beneficiaryPhoto = models.ImageField(upload_to='patientImg',blank=False, null=False)
    # lastDateToFund = models.CharField(max_length=100)
    # beneficiaryDocument = models.FileField(upload_to='documentImg',blank=False, null=False)
    created_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.frTitle)