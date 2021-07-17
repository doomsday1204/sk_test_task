import factory
from factory import fuzzy
from faker import Faker

from common.factories import BaseModelFactory
from products.models import Product, Category, Like, Comment
from users.tests.factories import UserFactory

fake = Faker()


class CategoryFactory(BaseModelFactory):
    name = factory.Sequence(lambda n: 'category {}'.format(n))
    slug = factory.Sequence(lambda n: 'category-{}'.format(n))

    class Meta:
        model = Category


class ProductFactory(BaseModelFactory):
    name = factory.Sequence(lambda n: 'product {}'.format(n))
    slug = factory.Sequence(lambda n: 'product-{}'.format(n))
    price = factory.fuzzy.FuzzyDecimal(10, 100)
    description = fake.text()
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product


class LikeFactory(BaseModelFactory):
    product = factory.SubFactory(ProductFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Like


class CommentFactory(BaseModelFactory):
    product = factory.SubFactory(ProductFactory)
    user = factory.SubFactory(UserFactory)
    text = fake.text()

    class Meta:
        model = Comment
