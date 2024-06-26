import factory

from .models.category import Category
from .models.product import Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    title = factory.Faker("pystr")
    category = factory.LazyAttribute(CategoryFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for categories in extracted:
                self.category.add(categories)

    class Meta:
        model = Product
        skip_postgeneration_save = True
