from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rivapp.views import InvoiceViewset,InvoiceDetailViewSet
from .views import my_public_view,invoice_details_view  # Import your custom view

router = DefaultRouter()
router.register(r'voices', InvoiceViewset)
router.register(r'invoicedetails', InvoiceDetailViewSet) 

urlpatterns = [
    path('voices/', include(router.urls)),  # Include your existing views
    path('public_view/', my_public_view, name='public-view'),  # Add your custom view
    path('invoicedetails/',invoice_details_view, name='create-invoice-with-details'),
]
