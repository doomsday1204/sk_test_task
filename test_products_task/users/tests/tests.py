from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.tests.factories import LikeFactory, CommentFactory
from users.tests.factories import UserFactory

User = get_user_model()

