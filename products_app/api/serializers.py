from rest_framework.serializers import ModelSerializer
from products_app.models import IndividualProduct

class InStockSerializer(ModelSerializer):
    class Meta:
        model = IndividualProduct
        fields = ['in_stock']

class AddProductSerializer(ModelSerializer):
    class Meta:
        model = IndividualProduct
        fields = '__all__'