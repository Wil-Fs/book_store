import pytest
from product.models import Product, Category

@pytest.mark.django_db
def test_product_creation():
    category = Category.objects.create(title='Categoria Teste', slug='categoria-teste')
    product = Product.objects.create(title='Produto Teste', price=100)
    product.category.add(category)

    assert product.title == 'Produto Teste'
    assert product.price == 100
    assert category in product.category.all()
