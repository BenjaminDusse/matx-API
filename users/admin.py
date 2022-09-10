from store.models import Product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from tags.models import TaggedItem
from users.models import User

class UserAdmin(BaseUserAdmin):
    pass

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

admin.site.register(User)