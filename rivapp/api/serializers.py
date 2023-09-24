from rest_framework.serializers import ModelSerializer
from rivapp.models import Invoice,InvoiceDetail

class InvoiceDetailSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'
    

class InvoiceSerializer(ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only = True)

    class Meta:
        model = Invoice
        fields = '__all__'
