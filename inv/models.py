from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
        name = models.CharField(
            max_length=200,
            verbose_name=_('name'))

        parent = TreeForeignKey('self',
            null=True,
            blank=True,
            related_name='children')

        class MPTTMeta:
            order_insertion_by = ['name']

        class Meta:
            verbose_name_plural = 'categories'

        def __unicode__(self):
            return self.name

class Room(models.Model):
        name = models.CharField(
            max_length=200,
            verbose_name=_('name'))

        def __unicode__(self):
            return self.name

class Item(models.Model):
        name = models.CharField(
            max_length=200,
            verbose_name=_('name'))

        room = models.ForeignKey(Room)

        storage = models.CharField(
            max_length=100,
            verbose_name=_('storage'))

        category = models.ForeignKey(Category,
            verbose_name=_('category'))

        owner = models.ForeignKey(User,
            blank=True,
            null=True,
            verbose_name=_('owner'),
            help_text=_('Item missing the owner are owned by hackerspace'))

        count = models.PositiveIntegerField(
            default=1,
            verbose_name=_('item count'))

        prize = models.PositiveIntegerField(
            default=0,
            verbose_name=_('item prize'))

        note = models.TextField(
            blank=True,
            verbose_name=_('note'))

        def __unicode__(self):
            return '%s (%s)' % (self.name, self.storage)
