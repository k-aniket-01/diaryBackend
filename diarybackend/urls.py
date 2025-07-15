from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ledger.views import *

router = DefaultRouter()
router.register(r'ledger-heads', LedgerHeadViewSet)
# Add others similarly...

urlpatterns = [
    path('api/', include(router.urls)),
]
