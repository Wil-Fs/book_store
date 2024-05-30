import pytest
from product.models import Category

@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(title='Categoria Teste', slug='categoria-teste')

    assert category.title == 'Categoria Teste'
    assert category.slug == 'categoria-teste'
    assert category.active is True