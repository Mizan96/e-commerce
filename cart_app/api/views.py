from rest_framework.generics import RetrieveUpdateAPIView 
from cart_app.models import Cart
from cart_app.api.serializers import CartSerializer

class CartApiView(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer