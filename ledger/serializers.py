# ledger/serializers.py
from rest_framework import serializers
from .models import LedgerHead, Party, Payment, Receipt, PartialPayment

class LedgerHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerHead
        fields = '__all__'

# Similar serializers for Party, Payment, etc.
