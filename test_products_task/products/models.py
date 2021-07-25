from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel
"""
Понимаю что сделал очень мало. Есть огромное желание учиться дальше
Спасибо за то что уделили время. Очень хотелось попытать свои силы и попасть на интернатуру

"""


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=False, editable=False)

    PARAMS = Choices(
        ('following', 'following'),
        ('price_to', 'price_to'),
        ('price_from', 'price_from'),
    )

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    GRADE_CHOICES = Choices(
        ('base', 'base', _('Base')),
        ('standard', 'standard', _('Standard')),
        ('premium', 'premium', _('Premium')),
    )

    name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=9)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='products')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',
                       args=[self.category.slug, self.slug])

    def save(self, *args, **kwargs):
        if self.pk is None:  # works on object creation only
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Like(TimeStampedModel):
    product = models.ForeignKey(Product, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='likes')
    ip = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        unique_together = (('product', 'user'), ('product', 'ip'))

    def __str__(self):
        return '{} from {}'.format(self.product, self.user or self.ip)


class Comment(TimeStampedModel):
    product = models.ForeignKey(Product, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='comments')
    ip = models.GenericIPAddressField(blank=True, null=True)
    text = models.TextField(_('Comment'))

    def __str__(self):
        return 'comment from {}'.format(self.user or self.ip)
