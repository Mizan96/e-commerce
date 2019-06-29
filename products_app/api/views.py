from rest_framework.generics import (
                                    UpdateAPIView, 
                                    RetrieveUpdateAPIView, 
                                    CreateAPIView
                                    )

from products_app.api.serializers import InStockSerializer, AddProductSerializer
from products_app.models import IndividualProduct

class InStockUpadteView(RetrieveUpdateAPIView):
    serializer_class = InStockSerializer
    queryset = IndividualProduct.objects.all() 

class AddProductView(CreateAPIView):
    queryset = IndividualProduct.objects.all()
    serializer_class = AddProductSerializer