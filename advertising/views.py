from rest_framework import viewsets
from .models.product import Product
from .serializers import ProductSerializer

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
