import pytest
from product.models import Product, Category
from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    category = Category.objects.create(title='Categoria Teste', slug='categoria-teste')
    product = Product.objects.create(title='Produto Teste', price=100)
    product.category.add(category)
    serializer = ProductSerializer(product)

    assert serializer.data['title'] == 'Produto Teste'
    assert serializer.data['price'] == 100
    assert 'category' in serializer.data
    assert serializer.data['category'][0]['title'] == 'Categoria Teste'