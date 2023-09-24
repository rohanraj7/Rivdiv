from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import render


@api_view(['GET'])
@permission_classes([AllowAny])
def my_public_view(request):
    return render(request, 'index.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def invoice_details_view(request):
    print("Workingggggg")
    pass
