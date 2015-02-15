from django.contrib import admin
from grey_rain.models import Item, ItemCategory, ItemSubcategory, ItemVariant, Customer, Carousel;

# Register your models here.
admin.site.register(Customer)
admin.site.register(Carousel)
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemSubcategory)
admin.site.register(ItemVariant)


