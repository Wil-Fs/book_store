import pytest
from product.models import Category
from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    category = Category.objects.create(title='Categoria Teste', slug='categoria-teste')
    serializer = CategorySerializer(category)

    assert serializer.data['title'] == 'Categoria Teste'
    assert serializer.data['slug'] == 'categoria-teste'
