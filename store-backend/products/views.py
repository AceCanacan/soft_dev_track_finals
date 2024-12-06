from rest_framework import viewsets 
from .models import Product, ProductImage
from .serializers import ProductImageSerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet): 
    # Define queryset to include only available products
    queryset = Product.objects.filter(available=True) 
      
    # Specify serializer to be used 
    serializer_class = ProductSerializer 

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

@api_view(['POST'])
@transaction.atomic
def checkout(request):
    cart = request.data.get('cart', [])
    if not cart:
        return Response({"message": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Process payment logic here (omitted for brevity)
    
    # After successful payment, mark products as unavailable
    product_ids = [item['id'] for item in cart]
    products = Product.objects.filter(id__in=product_ids, available=True)
    products.update(available=False)
    
    return Response({"message": "Checkout successful"}, status=status.HTTP_200_OK)

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context