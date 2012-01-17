from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from mptt.admin import MPTTModelAdmin
from mptt.forms import TreeNodeChoiceField

from models import Category, Item, Room

class ItemForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.tree.all(),
        level_indicator=mark_safe(u'&nbsp;&nbsp;&nbsp;'))
    class Meta:
        model = Item

class InlineForm(ItemForm):
    class Meta:
        model = Item
        widgets = {
            'name': forms.TextInput(attrs={'size': 50}),
            'storage': forms.TextInput(attrs={'size': 10}),
            'note': forms.TextInput(),
        }

class ItemInline(admin.TabularInline):
    model = Item
    form = InlineForm
    extra = 10

class ItemAdmin(admin.ModelAdmin):
    form = ItemForm

class RoomAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Room, RoomAdmin)
