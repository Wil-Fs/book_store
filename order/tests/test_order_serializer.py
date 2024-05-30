import pytest
from rest_framework.exceptions import ValidationError
from product.models import Product
from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    product = Product.objects.create(title='Produto Teste', price=100)
    order_data = {'product': [product]}

    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.validated_data['product'][0] == product
    assert 'total' in serializer.data
    assert serializer.data['total'] == product.price