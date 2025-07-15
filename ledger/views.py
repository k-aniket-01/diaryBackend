# ledger/views.py
from rest_framework import viewsets
from .models import LedgerHead, Party, Payment, Receipt, PartialPayment
from .serializers import *

class LedgerHeadViewSet(viewsets.ModelViewSet):
    queryset = LedgerHead.objects.all()
    serializer_class = LedgerHeadSerializer

# Add other ViewSets similarly
